from django.shortcuts import render
from django.http import HttpResponse

def show_home(request):
    return render(request,'index.html')

def show_intro(request):
    return HttpResponse("This in intro")

def show_contacts(request):
    return HttpResponse("This in contacts")

def show_policies(request):
    return HttpResponse("This in policies")

