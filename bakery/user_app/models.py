from django.db import models
from django.contrib.auth.models import User
from bakery_app.models import Product

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.firstname}'

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.customer}'

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    def __str__(self):
        return f'{self.cart}'
    def subprice(self):
        return self.product.price * self.amount
