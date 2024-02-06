from user_app.models import Cart, Customer ,CartDetail
from django.contrib.auth.models import User
from custom.check_exist import *
from user_order.models import Order, OrderDetail

def check_profile(newuser):
    try:
        customer = Customer.objects.get(user=newuser)
        return True
    except:
        return False

def check_cart(user):
    try:
        cart = Cart.objects.get(customer=user)
        detail = CartDetail.objects.filter(cart=cart).exists()
        return detail
    except:
        return False
    
def check_order(customer):
    try:
        order = Order.objects.get(customer=customer)
        detail = OrderDetail.objects.filter(order=order).exists()
        return detail
    except:
        return False