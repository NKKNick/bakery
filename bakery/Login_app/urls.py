from django.urls import path
from Login_app import views


urlpatterns = [
    path("login/",views.login_user ,name="login"),

]
