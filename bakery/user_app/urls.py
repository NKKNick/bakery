from django.urls import path
from bakery_app import views
from user_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("show_bakery/",views.show_bakery,name="show_bakery"),
    path("create_bakery/",views.create_bakery,name="create_bakery"),
    path("update_bakery/<int:id>/",views.update_bakery,name="update_bakery"),
    path("delete_bakery/<int:id>/",views.delete_bakery,name="delete_bakery"),
    path("user/profile",views.profile,name="profile"),
    path("user/update",views.update_profile,name="update_profile"),
    path("about/",views.about,name="about"),
    path("kuy",views.kuy,name="kuy"),
]
