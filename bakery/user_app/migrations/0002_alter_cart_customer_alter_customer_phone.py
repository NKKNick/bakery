# Generated by Django 4.2.7 on 2024-01-24 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.IntegerField(),
        ),
    ]