# Generated by Django 4.2.11 on 2024-05-17 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0008_rename_cost_expense_expense_cost_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoicedetail",
            name="price",
        ),
    ]