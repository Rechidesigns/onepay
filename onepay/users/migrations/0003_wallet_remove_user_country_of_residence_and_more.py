# Generated by Django 4.2.2 on 2023-06-28 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_options_user_contact_number_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wallet",
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
                        max_length=20,
                        verbose_name="Created Date",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Modified date when the record was created.",
                        max_length=20,
                        verbose_name="Modified Date",
                    ),
                ),
            ],
            options={
                "verbose_name": "Base Model",
                "verbose_name_plural": "Base Model",
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="country_of_residence",
        ),
        migrations.RemoveField(
            model_name="user",
            name="current_address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="user",
            name="default_currency",
        ),
        migrations.RemoveField(
            model_name="user",
            name="job_title",
        ),
        migrations.RemoveField(
            model_name="user",
            name="permanent_address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="place_of_birth",
        ),
        migrations.RemoveField(
            model_name="user",
            name="registered_ip_address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="social_security_number",
        ),
        migrations.RemoveField(
            model_name="user",
            name="verification_date",
        ),
        migrations.DeleteModel(
            name="UserAddress",
        ),
        migrations.AddField(
            model_name="wallet",
            name="wallet_id",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
