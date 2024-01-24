from django.urls import include, path

from user_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("user/cart",views.cart,name="cart"),
    path("user/profile",views.profile,name="profile"),
    path("",views.index,name="index"),
    path("",views.index,name="index"),
]
