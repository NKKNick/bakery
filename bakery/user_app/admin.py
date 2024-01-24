from django.contrib import admin
from user_app.models import Cart, CartDetail, Customer

# Register your models here.
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartDetail)