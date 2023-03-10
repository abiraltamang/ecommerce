from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from shopping.models import Comment


def show_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})


def searched_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})


def classified_products(request, genre, value):
    if genre == 'type':
        products = Product.objects.filter(type_id =value)
    if genre == 'sc':
        products = Product.objects.filter(type__subcategory_id =value)
    if genre == 'cat':
        products = Product.objects.filter(type__subcategory__category_id=value)
    if genre == 'brand':
        products = Product.objects.filter(brand_id = value)


    # products = Product.objects.all()
    return render(request, 'products.html', {'products':products})


def show_product_details(request, id):
    comments = Comment.objects.all()
    product = Product.objects.get(id=id)
    # return HttpResponse(product)
    return render(request, 'detail.html', {"product": product, "comments":comments})

