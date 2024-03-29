# Generated by Django 4.1.1 on 2022-10-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("references", "0007_book"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookSeries",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_series", models.IntegerField(verbose_name="Books in series")),
                (
                    "book_name",
                    models.CharField(max_length=30, verbose_name="Book name"),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]
