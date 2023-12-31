# Generated by Django 4.2.2 on 2023-07-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wallet", "0002_alter_wallet_pin_alter_wallet_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="wallettransaction",
            name="description",
            field=models.CharField(
                blank=True,
                help_text="Description/purpose of the transaction",
                max_length=50,
                null=True,
                verbose_name="Transaction Description",
            ),
        ),
        migrations.AlterField(
            model_name="wallettransaction",
            name="type",
            field=models.CharField(
                choices=[("payment", "payment"), ("Received", "Received")],
                help_text="The type of ctransaction performed",
                max_length=200,
                verbose_name="Type",
            ),
        ),
    ]
