from django.urls import path
from bakery_app import views
from user_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("เกี่ยวกับเรา/",views.about,name="about"),
    path("ขนมทั้งหมด/",views.show_bakery,name="show_bakery"),
    path("ผู้ใช้/โปรไฟล์",views.profile,name="profile"),
]
