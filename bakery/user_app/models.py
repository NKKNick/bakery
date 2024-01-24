from django.db import models
from django.contrib.auth.models import User
from bakery_app.models import Product

# Create your models here.
class CustomerProfile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
