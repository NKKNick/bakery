from django.shortcuts import render

# Create your views here.
def login_user(req):
    return render(req,"login_app/Login.html")