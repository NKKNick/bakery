# Generated by Django 4.2.7 on 2024-02-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0007_remove_orderdetail_order_delete_order_and_more"),
        ("user_order", "0002_order_slip"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="info",
        ),
        migrations.AlterField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user_app.customer"
            ),
        ),
    ]
