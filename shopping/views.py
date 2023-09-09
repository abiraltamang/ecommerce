from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from shopping.models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm

@login_required
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



@login_required
def remove_from_wishlist(request):
    pass


@login_required
def add_to_cart(request, pid, qty):
    cart = Cart.objects.filter(user=request.user).filter(product_id=pid)
    if not cart:
        cart = Cart(user=request.user, product=Product.objects.get(id=pid), qty=qty)
        cart.save()
        messages.info(request, 'Item added to you Cart!')
    else:
        messages.info(request, 'Item already exists in your Cart!')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
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

    
@login_required
def remove_from_cart(request):
    pass


@login_required
def comment(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        cmt = request.POST['comment']

        comment = Comment(user=request.user, product_id=pid, comment=cmt)
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    


@login_required
def show_wishlist(request):
    wishlist = Wishlist.objects.filter( user = request.user)
    return render(request, 'wishlist.html', {'wishlist':wishlist})
    


@login_required
def show_cart(request):
    cart = Cart.objects.filter(user = request.user)
    return render (request, 'cart.html', {'cart':cart})


@login_required
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
        # dt['discount']=c.product.discount
        total += dt['amount'] 
        data.append(dt)

    print(data)
    print(total)

    return render (request, 'checkout.html', {'data':data, 'total':total})

@login_required
def review(request):
    pass

def payment_view(request):
    paypal_dict = {
        'business': 'sb-aevsb26410777@personal.example.com',
        'amount': '100.00',
        'item_name': 'Test Item',
        'invoice': 'unique-invoice-id',
        'currency_code': 'USD',
        'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
        'return_url': request.build_absolute_uri(reverse('payment_success')),
        'cancel_return': request.build_absolute_uri(reverse('payment_cancel')),
        'custom': 'Extra data',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form}
    return render(request, 'payment.html', context)

@csrf_exempt
def payment_success(request):
    # Process successful payment
    return render(request, 'payment_success.html')

def payment_cancel(request):
    # Handle payment cancellation
    return render(request, 'payment_cancel.html')


