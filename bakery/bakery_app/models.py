from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField(default=0)
    descriptions = models.CharField(max_length=100,blank=True)
    category = models.CharField(max_length=1000,blank=True)
    image = models.ImageField(upload_to="product",blank=True)

    def str(self):
        return f'{self.name} {self.price} {self.amount} {self.descriptions} {self.category} {self.image}'