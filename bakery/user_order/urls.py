from django.urls import path
from user_order import views


urlpatterns = [
    path("รายการ",views.confirm_order,name="order"),
    path("รายการ/คิวอาร์",views.upload_slip,name="qr"),
    path("รายการ/ประวัติ",views.order_history,name="order_history"),
    path("รายการ/รายละเอียด/<int:id>",views.order_detail,name="order_detail"),
]