# Generated by Django 4.2.11 on 2024-05-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0003_rename_customer_points_customer_customer_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="customer_contact",
            field=models.CharField(max_length=255),
        ),
    ]