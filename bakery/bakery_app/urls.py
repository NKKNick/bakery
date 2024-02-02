from django.urls import path

from bakery_app import views


urlpatterns = [
    path("cart",views.cart,name='cart'),
    path("cart/delete/<int:id>",views.delete_cart,name='cart_delete'),
    path("cart/add/<int:id>",views.add_cart,name='cart_add'),
    path("cart/dec/<int:id>",views.dec_cart,name='cart_dec'),
    path("cart/inc/<int:id>",views.inc_cart,name='cart_inc'),

]



