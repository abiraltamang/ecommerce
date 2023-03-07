from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from contents.models import Content

def show_home(request):
    latest_products = Product.objects.order_by('-id')[:2]
    sliders = Content.objects.filter(section__title = 'slider')
    return render(request,'index.html', {'sliders' : sliders, 'latest': latest_products})

def show_content(request, section):
    data = Content.objects.filter(section__title = section)
    return render(request, 'content.html', {'data': data})

def show_about(request):
    about = Content.objects.filter(section__title = 'About')
    return HttpResponse(about)


def show_contacts(request):
    about = Content.objects.filter(section_id=1)
    return HttpResponse("This in contacts")

def show_policies(request):
    return HttpResponse("This in policies")

