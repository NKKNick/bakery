from http.client import HTTPResponse
from django.shortcuts import redirect, render
from user_app.forms import CustomerForm
from bakery_app.models import Product
from django.contrib.auth.decorators import login_required
from user_app.models import Cart, CartDetail

# Create your views here.
def index(req):
<<<<<<< HEAD
    return HTTPResponse("asdawdawd")

@login_required
def profile(req):
    if req.method == "POST":
        form = CustomerForm(req.POST,instance=req.user)
        if form.is_valid():
            form.save()
            return redirect("/user/cart")
    else:
        form = CustomerForm()
    return render(req,'bakery/userprofile.html',{'form':form})

@login_required
def cart(request):
    count = 0
    total = 0
    try:
        cart = Cart.objects.get(customer=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(customer=request.user)

    try:
        cart_detail = CartDetail.objects.filter(cart=cart)
        for detail in cart_detail:
            count += detail.amount  
            total += detail.product.price * detail.amount
            
    except CartDetail.DoesNotExist:
        cart = None
        cart_detail = None

    return render(request, "bakery/cart.html", {'count': count, 'total': total, 'cartDetail': cart_detail})

@login_required
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
        if cart_detail.amount < cart_detail.product.stock:
            cart_detail.amount += 1
            cart_detail.save()
            return redirect('/')

    except CartDetail.DoesNotExist:
        cart_detail = CartDetail.objects.create(
            product=product,
            cart=cart,
            amount=1,
        )
        return redirect('/')

@login_required
def delete_cart(req,id):
    product = Product.objects.get(pk=id)
    cart = Cart.objects.get(customer=req.user)
    cartDetail=CartDetail.objects.get(product=product,cart=cart)
    cartDetail.delete()
    return redirect("/cart")
=======
    return render(req , "bakery/index.html")

def test(req):
    return render(req , "bakery/about.html")
>>>>>>> c9674202030136d297220ae3be956e7871114653
