# Generated by Django 4.2.7 on 2024-02-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="slip",
            field=models.ImageField(blank=True, upload_to="slip"),
        ),
    ]