# Generated by Django 4.2.13 on 2024-05-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0014_customer_customer_is_delete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_amount',
            field=models.FloatField(default=0),
        ),
    ]