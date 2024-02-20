from django.shortcuts import redirect, render
from user_app.models import Cart,CartDetail, Customer
from custom.check_exist import check_profile
from django.contrib.auth.decorators import login_required

from user_order.models import Order, OrderDetail

# Create your views here.
@login_required(login_url='/login')
def confirm_order(req):
    if check_profile(req.user):
        custome= Customer.objects.get(user=req.user)
        cart = Cart.objects.get(customer=req.user)
        cdetail= CartDetail.objects.filter(cart=cart)
        total = 0
        total_amount = 0
        for i in cdetail:
            total += i.product.price * i.amount
            total_amount += i.amount
        
        return render(req,'order.html',{'customer':custome,'total':total,'cart':cdetail,'total_amount':total_amount})
    else:
        return redirect('/user/profile')

def upload_slip(req):
    if req.method == "POST":
        image = req.FILES.get('image')
        customer = Customer.objects.get(user=req.user)
        cart = Cart.objects.get(customer=req.user)
        cdetail= CartDetail.objects.filter(cart=cart)
        total = 0
        for i in cdetail:
            total += i.product.price * i.amount
        if image:
            order = Order.objects.create(
                customer = customer,
                total = total,
                address = customer.address,
                slip = image,
            )
            order.save()

        for i in cdetail:
            orderdetail = OrderDetail.objects.create(
                order = order,
                product = i.product.name,
                amount = i.amount,
                price = i.product.price,
            )
            orderdetail.save()
        cart.delete()
        return redirect('/')

    else:
        return render(req,'showqr.html')