# Generated by Django 4.1.1 on 2022-12-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "catalog",
            "0002_appuser_additional_info_appuser_address_appuser_city_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="index",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
