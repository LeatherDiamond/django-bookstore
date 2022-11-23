# Generated by Django 4.1.1 on 2022-11-22 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("carts", "0013_remove_cart_good_remove_cart_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Cart",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Carts",
            ),
        ),
    ]
