# Generated by Django 4.2.7 on 2024-02-05 13:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_order", "0003_remove_order_info_alter_order_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderdetail",
            name="order",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderDetail",
        ),
    ]
