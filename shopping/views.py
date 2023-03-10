from django.shortcuts import render, redirect
from django.contrib import messages
from shopping.models import *
from datetime import datetime

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


def add_to_cart(request, pid, qty):
    cart = Cart.objects.filter(user=request.user).filter(product_id=pid)
    if not cart:
        cart = Cart(user=request.user, product=Product.objects.get(id=pid), qty=qty)
        cart.save()
        messages.info(request, 'Item added to you Cart!')
    else:
        messages.info(request, 'Item already exists in your Cart!')
    return redirect(request.META.get('HTTP_REFERER'))

def add_to_cart_form(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        qty = request.POST['qty']

        cart = Cart.objects.filter(user=request.user).filter(product_id=pid)

        if not cart:
            cart = Cart(user=request.user, product=Product.objects.get(id=pid), qty=qty)
            cart.save()
            messages.info(request, 'Item added to you Cart!')
        else:
            messages.info(request, 'Item already exists in your Cart!')
        return redirect(request.META.get('HTTP_REFERER'))

    

def remove_from_cart(request):
    pass



def comment(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        cmt = request.POST['comment']

        comment = Comment(user=request.user, product_id=pid, comment=cmt)
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    

def show_wishlist(request):
    wishlist = Wishlist.objects.filter( user = request.user)
    return render(request, 'wishlist.html', {'wishlist':wishlist})
    



def show_cart(request):
    cart = Cart.objects.filter(user = request.user)
    return render (request, 'cart.html', {'cart':cart})



def checkout(request):
    cart = Cart.objects.filter(user = request.user)

    if request.method == 'POST':
        mob=request.POST['mobile']
        address= request.POST['address']
        for c in cart:
            order = Order(user = request.user, mobile=mob, address=address, product = c.product, 
                          qty= c.qty, price = c.product.price, date = datetime.now(), discount = c.product.discount)
            order.save()
        
        messages.success(request, 'Your order is placed')
        return redirect('home')


    data = []
    total = 0
    for c in cart:
        dt= {}
        dt['name'] = c.product.name
        dt['price'] = c.product.price
        dt['qty'] = c.qty
        dt['amount'] = float(c.qty) * float(c.product.price)
        total += dt['amount']
        data.append(dt)

    print(data)
    print(total)

    return render (request, 'checkout.html', {'data':data, 'total':total})


def review(request):
    pass