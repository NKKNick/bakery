from django.urls import path
from bakery_app import views
from user_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("show_bakery/",views.show_bakery,name="show_bakery"),
    path("user/profile",views.profile,name="profile"),
]
