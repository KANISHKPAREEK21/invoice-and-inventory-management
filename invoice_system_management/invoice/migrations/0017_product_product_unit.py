# Generated by Django 4.2.11 on 2024-06-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0016_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_unit",
            field=models.CharField(default=1, max_length=255),
        ),
    ]