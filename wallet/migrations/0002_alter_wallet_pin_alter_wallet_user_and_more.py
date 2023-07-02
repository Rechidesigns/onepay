# Generated by Django 4.2.2 on 2023-07-02 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="pin",
            field=models.CharField(
                default="0000", help_text="The PIN of the customer.", max_length=4, verbose_name="Card Pin"
            ),
        ),
        migrations.AlterField(
            model_name="wallet",
            name="user",
            field=models.OneToOneField(
                help_text="The user detail that owns the wallet",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User Wallet",
            ),
        ),
        migrations.AlterField(
            model_name="wallet",
            name="wallet_id",
            field=models.CharField(
                help_text="The wallet ID of the user which serves as a the account number of the wallet",
                max_length=10,
                unique=True,
                verbose_name="Wallet ID",
            ),
        ),
        migrations.AlterField(
            model_name="wallettransaction",
            name="amount",
            field=models.DecimalField(
                decimal_places=2,
                help_text="The amount of the transaction in figures",
                max_digits=100,
                verbose_name="Amount",
            ),
        ),
        migrations.AlterField(
            model_name="wallettransaction",
            name="reference",
            field=models.CharField(
                help_text="The holds the reference of the transactions",
                max_length=50,
                verbose_name="Transaction Reference",
            ),
        ),
        migrations.AlterField(
            model_name="wallettransaction",
            name="status",
            field=models.CharField(
                default="pending", help_text="The status of the transaction", max_length=15, verbose_name="Status"
            ),
        ),
        migrations.AlterField(
            model_name="wallettransaction",
            name="type",
            field=models.CharField(
                choices=[("deposit", "deposit"), ("transfer", "transfer"), ("withdraw", "withdraw")],
                help_text="The type of ctransaction performed",
                max_length=200,
                verbose_name="Type",
            ),
        ),
        migrations.AlterField(
            model_name="wallettransaction",
            name="wallet",
            field=models.ForeignKey(
                help_text="The wallet ID of the transaction",
                on_delete=django.db.models.deletion.CASCADE,
                to="wallet.wallet",
                verbose_name="Wallet Transaction",
            ),
        ),
        migrations.CreateModel(
            name="UpComingPayment",
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
                ("name", models.CharField(help_text="The purpose of the payment", max_length=50, verbose_name="Name")),
                (
                    "status",
                    models.CharField(
                        default="pending",
                        help_text="The status of the transaction",
                        max_length=15,
                        verbose_name="Status",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The amount of the transaction in figures",
                        max_digits=100,
                        verbose_name="Amount",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="this holds the user scheduling the payment",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User Upcoming payment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Up-Coming Payment",
                "verbose_name_plural": "Up-Coming Payments",
            },
        ),
        migrations.CreateModel(
            name="PaymentRequest",
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
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The amount requested for payment",
                        max_digits=10,
                        verbose_name="Amount",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Description of the payment request or invoice", verbose_name="Description"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="pending",
                        help_text="The status of the transaction",
                        max_length=15,
                        verbose_name="Status",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        help_text="The user receiving the payment request",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_payment_requests",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Recipient",
                    ),
                ),
                (
                    "requester",
                    models.ForeignKey(
                        help_text="The user requesting the payment",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_requests",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Requester",
                    ),
                ),
            ],
            options={
                "verbose_name": "Payment Request",
                "verbose_name_plural": "Payment Requests",
            },
        ),
        migrations.CreateModel(
            name="Beneficiary",
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
                    "name",
                    models.CharField(
                        help_text="The name of the beneficiary", max_length=100, verbose_name="Beneficiary Name"
                    ),
                ),
                (
                    "account_number",
                    models.CharField(
                        help_text="The account number of the beneficiary", max_length=20, verbose_name="Account Number"
                    ),
                ),
                (
                    "bank_name",
                    models.CharField(
                        help_text="The name of the bank where the beneficiary's account is held",
                        max_length=100,
                        verbose_name="Bank Name",
                    ),
                ),
                (
                    "wallet",
                    models.ForeignKey(
                        help_text="The wallet associated with the beneficiary",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wallet.wallet",
                        verbose_name="Wallet",
                    ),
                ),
            ],
            options={
                "verbose_name": "Beneficiary",
                "verbose_name_plural": "Beneficiary",
            },
        ),
    ]
