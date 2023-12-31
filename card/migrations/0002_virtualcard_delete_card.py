# Generated by Django 4.2.2 on 2023-07-02 17:57

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("card", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VirtualCard",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="this is the unique identifier of an object",
                        primary_key=True,
                        serialize=False,
                        verbose_name="id",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Timestamp when the record was created.",
                        verbose_name="Created Date",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Modified date when the record was created.",
                        verbose_name="Modified Date",
                    ),
                ),
                (
                    "card_number",
                    models.CharField(
                        help_text="The card number of the virtual card", max_length=16, verbose_name="Card Number"
                    ),
                ),
                (
                    "card_name",
                    models.CharField(
                        blank=True, help_text="Card holder name", max_length=200, null=True, verbose_name="Card Name"
                    ),
                ),
                ("cvv", models.IntegerField(help_text="Card Verification Value", verbose_name="CVV")),
                (
                    "expiration_date",
                    models.DateField(
                        help_text="The expiration date of the virtual card", verbose_name="Expiration Date"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Indicates whether the virtual card is active or not",
                        verbose_name="Active",
                    ),
                ),
            ],
            options={
                "verbose_name": "Card",
                "verbose_name_plural": "Cards",
            },
        ),
        migrations.DeleteModel(
            name="Card",
        ),
    ]
