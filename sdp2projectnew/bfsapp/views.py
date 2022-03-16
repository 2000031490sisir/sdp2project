from django.shortcuts import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('we are in the root dir')


def homescreen(request):
    return render(request, "homescreen.html")


def homescreencss(request):
    return render(request, "homescreen.css")


def home(request):
    return render(request, "Home.html")


def login(request):
    return render(request, "login.html")


def newuser(request):
    return render(request, "newuser.html")


def validations(request):
    return render(request, "validations.js")


def bfspython(request):
    return render(request, "bfsapp.py")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
