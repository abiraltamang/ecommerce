from django.shortcuts import render
from django.contrib import messages
from shopping.models import *
from django.shortcuts import redirect

def add_to_wishlist(request,  pid):
    wl = Wishlist.objects.filter(user= request.user).filter(product_id=pid)
    if not wl:
        # wl = Wishlist(user_id =  request.user.id, product_id=pid)
        wl = Wishlist(user =  request.user, product= Product.objects.get(id=pid))
        wl.save()
        messages.info(request, 'Item added to your wishlist')
    else:
        messages.info(request, 'Item already added to your wishlist')

    return redirect('home')
    

def remove_from_wishlist(request):
    pass


def add_to_cart(request):
    pass


def remove_from_cart(request):
    pass


def checkout(request):
    pass


def comment(request):
    pass


def review(request):
    pass