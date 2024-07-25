from django.http import HttpResponse


def hello_word(request):
    return HttpResponse("Hello World")


def root_folder(requests):
    return HttpResponse("This is the root folder")