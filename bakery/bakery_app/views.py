from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from bakery_app.models import Product
from user_app.models import Cart, CartDetail
# Create your views here.

@login_required(login_url='/login')
def cart(request):
    count = 0
    total = 0
    shipping_cost = 0 
    try:
        cart = Cart.objects.get(customer=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(customer=request.user)

    try:
        cart_detail = CartDetail.objects.filter(cart=cart)
        for detail in cart_detail:
            count += detail.amount  
            total += detail.product.price * detail.amount
            
        shipping_cost = total // 10
            
    except CartDetail.DoesNotExist:
        cart = None
        cart_detail = None

    return render(request, "cart.html", {'count': count, 'total': total, 'cart_detail': cart_detail, 'shipping_cost': shipping_cost})


@login_required(login_url='/login')
def add_cart(req, id):
    product = Product.objects.get(pk=id)
    try:
        # ดึงข้อมูลที่มีอยู่แล้ว
        cart = Cart.objects.get(customer=req.user)
    except Cart.DoesNotExist:
        # ถ้าไม่มีสร้างใหม่
        cart = Cart.objects.create(customer=req.user)
        
    try:
        cart_detail = CartDetail.objects.get(product=product, cart=cart)
        if cart_detail.amount < cart_detail.product.amount:
            cart_detail.amount += 1
            cart_detail.save()
            return redirect('/show_bakery')
        else:
            return redirect('/show_bakery')

    except CartDetail.DoesNotExist:
        cart_detail = CartDetail.objects.create(
            product=product,
            cart=cart,
            amount=1,
        )
        return redirect('/show_bakery')

@login_required(login_url='/login')
def dec_cart(req,id):
    product =Product.objects.get(pk=id)
    cart = Cart.objects.get(customer=req.user)
    cart_detail = CartDetail.objects.get(product=product, cart=cart)
    if cart_detail.amount <= 1 :
        return redirect('/cart')
    else :
        cart_detail.amount -= 1
        cart_detail.save()
        return redirect('/cart')

@login_required(login_url='/login')
def inc_cart(req,id):
    product =Product.objects.get(pk=id)
    cart = Cart.objects.get(customer=req.user)
    cart_detail = CartDetail.objects.get(product=product, cart=cart)
    if cart_detail.amount < cart_detail.product.amount :
        cart_detail.amount += 1
        cart_detail.save()
        return redirect('/cart')
    else :
        return redirect('/cart')


@login_required(login_url='/login')
def delete_cart(req,id):
    product = Product.objects.get(pk=id)
    cart = Cart.objects.get(customer=req.user)
    cartDetail=CartDetail.objects.get(product=product,cart=cart)
    cartDetail.delete()
    return redirect("/cart")