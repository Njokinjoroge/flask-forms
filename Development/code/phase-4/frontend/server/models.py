from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Traveler(db.Model):
    __tablename__ = 'travelers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships

def to_dict(self):
        return {
            'id': self.id,
            'name': self.username,
            'email': self.email,
            'created_at': self.created_at
        }

def __repr__(self):
        return f'<Traveler {self.username} created.>'