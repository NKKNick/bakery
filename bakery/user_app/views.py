from http.client import HTTPResponse
from django.shortcuts import redirect, render
from user_app.forms import CustomerForm
from bakery_app.models import Product
from django.contrib.auth.decorators import login_required
from user_app.models import Cart, CartDetail, Customer

# Create your views here.
def index(req):
    return render(req , "bakery/index.html")

def test(req):
    return render(req , "bakery/about.html")

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                # Check if a Customer record already exists for the user
                existing_customer = Customer.objects.filter(user=request.user).first()

                if existing_customer:
                    # Handle the case where a Customer record already exists
                    return redirect('profile')  # Redirect to the user's profile or another view
                else:
                    # Create a new Customer record
                    customer = form.save(commit=False)
                    customer.user = request.user
                    customer.save()
                    # ... rest of your code
                    return redirect('/')  # Redirect to the home page or another view
            else:
                return redirect('login')
        else:
            print(form.errors)
            # Handle form errors or display them in the template
    else:
        form = CustomerForm()

    return render(request, 'bakery/userprofile.html', {'form': form})

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

    return render(request, "bakery/cart.html", {'count': count, 'total': total, 'cart_detail': cart_detail})

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
