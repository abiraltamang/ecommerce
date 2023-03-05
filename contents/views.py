from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from contents.models import Content

def show_home(request):
    latest_products = Product.objects.order_by('-id')[:2]
    sliders = Content.objects.filter(section_id=4)
    # return HttpResponse(latest_products)
    return render(request,'index.html', {'sliders' : sliders, 'latest': latest_products})

def show_intro(request):
    return HttpResponse("This in intro")

def show_contacts(request):
    return HttpResponse("This in contacts")

def show_policies(request):
    return HttpResponse("This in policies")

