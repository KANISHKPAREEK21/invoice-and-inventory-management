# Generated by Django 4.2.13 on 2024-05-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0011_remove_invoice_price_invoicedetail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
