from http.client import HTTPResponse
from django.shortcuts import redirect, render
from custom.check_exist import check_profile
from user_app.forms import CustomerForm
from bakery_app.models import Product
from django.contrib.auth.decorators import login_required,permission_required
from user_app.models import Cart, CartDetail, Customer
from bakery_app.forms import BakeryForm
from django.contrib.auth.models import User

# Create your views here.
def index(req):
    return render(req , "index.html")

def about(req):
    return render(req , "about.html")

@login_required
def kuy(req):
    if check_profile(req.user):
        return redirect('update')
    else:
        return redirect('user/profile')


@login_required
def profile(req):
    if req.method == 'POST':
        form = CustomerForm(req.POST)
        if form.is_valid():
            if req.user.is_authenticated:
                # Check if a Customer record already exists for the user
                existing_customer = Customer.objects.filter(user=req.user).first()

                if existing_customer:
                    customer = Customer.objects.get(user=req.user)
                    form = CustomerForm(req.POST, instance=customer)
                    if form.is_valid():
                        form.instance.owner = req.user
                        form.save()
                        return render(req,'updatecustomer.html',{'customer':customer})
                else:
                    # Create a new Customer record
                    customer = form.save(commit=False)
                    customer.user = req.user
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

    return render(req, 'userprofile.html', {'form': form})

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

    return render(request, "cart.html", {'count': count, 'total': total, 'cart_detail': cart_detail})

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

def show_bakery(req):
    bakeries = Product.objects.all()
    return render(req, 'show_bakery.html', {'bakeries':bakeries})

@permission_required('admin',login_url="/")
@login_required
def create_bakery(req):
    form = BakeryForm()
    if req.method == 'POST':
        form = BakeryForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        redirect("/")
    return render(req, 'create_bakery.html', {'form':form})

@login_required
def update_bakery(req,id):
    bakeries = Product.objects.get(pk=id)
    form = BakeryForm(req.POST, instance=bakeries)
    if form.is_valid():
        form.instance.owner = req.user
        form.save()
        return redirect('/')
    return render(req, 'update_bakery.html', {'fic':bakeries})

@login_required
def delete_bakery(req,id):
    bakeries = Product.objects.get(pk=id)
    bakeries.delete()
    return redirect('/')