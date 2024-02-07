from django.urls import path
from user_order import views


urlpatterns = [
    path("order",views.create_order,name="order"),
    path("order/qr",views.upload_slip,name="qr"),
]