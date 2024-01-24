from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req , "bakery/index.html")

def test(req):
    return render(req , "bakery/about.html")