# Generated by Django 4.1.1 on 2022-11-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0011_cart_good"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="quantity",
            field=models.PositiveIntegerField(default=1, verbose_name="quantity"),
            preserve_default=False,
        ),
    ]
