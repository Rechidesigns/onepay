# Generated by Django 4.2.2 on 2023-07-05 18:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wallet", "0003_wallettransaction_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="beneficiary",
            name="wallet",
        ),
    ]
