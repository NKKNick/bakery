from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    image = models.ImageField(upload_to="product",blank=True)

    def __str__(self):
        return f'{self.name} ราคา {self.price} บาท สั่งได้สูงสุด {self.amount} ชิ้น'
    
