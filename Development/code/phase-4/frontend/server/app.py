from flask import Flask, session, make_response, jsonify, request
from models import db, Traveler
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS 
import os

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0
app.secret_key =b'\x02\x0e\x9f-{]w\xf9\xe49\xde\xb6-\x94\\\xac'

api = Api(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Voyage</h1>'

class TravelerResource(Resource):
    def get(self, id=None):
        if id:
            user = Traveler.query.get(id)
            if not user:
                return {'error': 'Traveler not found.'}, 404
            return make_response(jsonify(user.to_dict())), 200
        else:
            users = Traveler.query.all()
            if not users:
                return {'error': 'There are no users to display.'}, 400
            return make_response(jsonify([u.to_dict() for u in users]), 200)
        

    def post(self):
        data = request.get_json()
        new_user = Traveler(
            username = data['name'],
            email = data['email'],
            password=data['password']
        )    

        db.session.add(new_user)
        db.session.commit()
        return {'success': 'Traveler created successfully'}, 201
    
    def patch(self, id):
        user = Traveler.query.filter_by(id=id).first()
        if not user:
            return {'error': 'Traveler not found.'}, 404
        data = request.json
        for attr in request.form():
            setattr(user, attr, request.form['attr'])
        db.session.commit()
        return {'success': 'Customer updated successfully.'}, 200
    
    def delete(self, id):
        user = Traveler.query.get(id)
        if not user:
            return {'error': 'Traveler not found.'}, 404
        db.session.delete(user)
        db.session.commit()
        return {}, 204
    
class Login(Resource):

    def post(self):
        user = Traveler.query.filter(
            Traveler.email == request.get_json()['email']
        ).first()

        session['user_id'] = user.id
        if not user:
            return {'error': 'User not found.'}, 404
        return {'message': 'successful!'}, 200
    
# class CheckSession(Resource):
#     def get(self):
#         user = Traveler.query.filter(Traveler.id == session.get('user_id')).first()
#         if user:
#             return user.to_dict()
#         else:
#             return {}, 401
api.add_resource(TravelerResource, '/travelers', '/travelers/<int:id>')
# api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(port=5555, debug=1)
