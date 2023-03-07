from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return  HttpResponse("Hello")


def register(request):
    if request.method == 'POST':
        return HttpResponse("Hello i am register")
    return HttpResponse('Invalid Access')