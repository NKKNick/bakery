from django.db import models
from django.contrib.auth.models import User
from user_app.models import Customer

#ยังไม่ชำระเงิน
#รอตรวจสอบสลิป
#ชำระเสร็จสิ้น
#ส่งสลิปใหม่

ORDER_CHOICE = (
    ("1","ยังไม่ชำระเงิน"),
    ("2","รอตรวจสอบสลิป"),
    ("3","ชำระเงินเสร็จสิ้น"),
    ("4","ส่งสลิปใหม่"),
)
# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    status = models.CharField(max_length=255,choices=ORDER_CHOICE,default=1)
    created = models.DateTimeField(auto_now_add =True)
    update = models.DateTimeField(auto_now =True)
    def __str__(self):
        return f'{self.customer}'
    
class OrderDetail(models.Model):
    product = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

class Payment(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add =True)
    update = models.DateTimeField(auto_now =True)
    slip = models.ImageField(upload_to='slip',blank=True)
    def __str__(self) -> str:
        return f'{self.order.customer}'



