# Generated by Django 4.2.11 on 2024-06-12 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0017_product_product_unit"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoicedetail",
            name="unit",
            field=models.IntegerField(null=True),
        ),
    ]