from django.urls import path
from admin_app import views


urlpatterns = [
    path("dashboard",views.testHello,name='dashboard'),
    path("create_bakery/",views.create_bakery,name="create_bakery"),
    path("update_bakery/<int:id>/",views.update_bakery,name="update_bakery"),
    path("delete_bakery/<int:id>/",views.delete_bakery,name="delete_bakery"),
    path("dashboard/order_admin",views.order_admin,name="order_admin"),
    path("dashboard/orderdetail/<int:id>",views.orderdetail_admin,name="orderdetail_admin"),
    path("dashboard/update/<int:id>",views.update_status,name="status_update"),
]