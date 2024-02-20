from django.urls import path
from admin_app import views


urlpatterns = [
    path("dashboard",views.testHello,name='dashboard'),
    path("create_bakery/",views.create_bakery,name="create_bakery"),
    path("update_bakery/<int:id>/",views.update_bakery,name="update_bakery"),
    path("delete_bakery/<int:id>/",views.delete_bakery,name="delete_bakery"),
]