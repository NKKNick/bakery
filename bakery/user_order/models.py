from django.db import models
from django.contrib.auth.models import User
from user_app.models import Customer

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    slip = models.ImageField(upload_to='slip',blank=True)
    def __str__(self):
        return f'{self.customer}'
    
class OrderDetail(models.Model):
    product = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)