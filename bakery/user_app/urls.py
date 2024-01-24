from django.urls import include, path

from user_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("",views.index,name="index"),
    path("",views.index,name="index"),
    path("",views.index,name="index"),
    path("about/",views.test,name="about"),
]
