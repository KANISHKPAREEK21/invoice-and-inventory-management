# Generated by Django 4.2.11 on 2024-05-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0004_alter_customer_customer_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="product_unit",
        ),
        migrations.AddField(
            model_name="invoicedetail",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
