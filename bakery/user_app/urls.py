from django.urls import include, path
from bakery_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("show_bakery/",views.show_bakery,name="show_bakery"),
    path("create_bakery/",views.create_bakery,name="create_bakery"),
    path("update_bakery/<int:id>/",views.update_bakery,name="update_bakery"),
    path("delete_bakery/<int:id>/",views.delete_bakery,name="delete_bakery"),
]