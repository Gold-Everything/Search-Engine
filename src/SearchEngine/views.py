from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world. This is the index page.")

def error(request):
    return HttpResponse(1/0)