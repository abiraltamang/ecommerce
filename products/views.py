from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_products(request):
    return HttpResponse('<h2> Hello World, i  am view from product page </h2> ')


def show_products(request):
    return render(request, 'products.html')