from user_app.models import Customer
from django.contrib.auth.models import User


def check_profile(newuser):
    try:
        customer = Customer.objects.get(user=newuser)
        return True
    except:
        return False