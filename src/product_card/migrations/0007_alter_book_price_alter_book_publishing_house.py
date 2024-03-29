# Generated by Django 4.1.1 on 2022-10-10 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("references", "0012_alter_bookgenre_genre_name_and_more"),
        ("product_card", "0006_alter_book_author_alter_book_genre_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Currncy in BYN",
                max_digits=5,
                verbose_name="Price",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="publishing_house",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="references.bookpublishinghouse",
                verbose_name="Publishing house",
            ),
        ),
    ]
