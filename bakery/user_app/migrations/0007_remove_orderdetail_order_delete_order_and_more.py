# Generated by Django 4.2.7 on 2024-02-02 08:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0006_order_orderdetail"),
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
