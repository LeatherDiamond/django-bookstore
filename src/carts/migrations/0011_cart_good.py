# Generated by Django 4.1.1 on 2022-11-21 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product_card", "0011_book_description"),
        ("carts", "0010_alter_cart_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="good",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="good",
                to="product_card.book",
                verbose_name="good",
            ),
            preserve_default=False,
        ),
    ]
