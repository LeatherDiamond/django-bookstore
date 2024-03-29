# Generated by Django 4.1.1 on 2022-11-22 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0014_alter_cart_customer"),
        ("order", "0005_alter_order_contact_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="cart",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                to="carts.cart",
                verbose_name="Order",
            ),
        ),
    ]
