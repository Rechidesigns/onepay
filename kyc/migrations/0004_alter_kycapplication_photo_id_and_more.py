# Generated by Django 4.2.2 on 2023-07-06 14:30

from django.db import migrations, models
import kyc.models


class Migration(migrations.Migration):
    dependencies = [
        ("kyc", "0003_alter_kycapplication_photo_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kycapplication",
            name="photo_id",
            field=models.FileField(
                help_text="The front side of The user's Photo Identitification. Chosen credential must not be expired. Document should be good condition and clearly visible. File is at least 1 MB in size and has at least 300 dpi resolution.",
                upload_to=kyc.models.KycApplication.generate_filename,
                verbose_name="Photo ID(front)",
            ),
        ),
        migrations.AlterField(
            model_name="kycapplication",
            name="photo_id_back",
            field=models.FileField(
                blank=True,
                help_text="The back side of The user's Photo Identitification. Chosen credential must not be expired. Document should be good condition and clearly visible. File is at least 1 MB in size and has at least 300 dpi resolution.",
                null=True,
                upload_to=kyc.models.KycApplication.generate_filename,
                verbose_name="Photo ID(back)",
            ),
        ),
        migrations.AlterField(
            model_name="kycapplication",
            name="proof_of_address_document",
            field=models.FileField(
                help_text="The document must contain your name, the address and should not be older than 90 days. Chosen credential must not be expired. Document should be good condition and clearly visible. File is at least 1 MB in size and has at least 300 dpi resolution.",
                upload_to=kyc.models.KycApplication.generate_filename,
                verbose_name="Proof of Address",
            ),
        ),
        migrations.AlterField(
            model_name="kycapplication",
            name="selfie_with_id",
            field=models.FileField(
                blank=True,
                help_text="Upload a photo with yourself and your Passport or both sides of the ID Card. The face and the document must be clearly visible.",
                null=True,
                upload_to=kyc.models.KycApplication.generate_filename,
                verbose_name="Selfie with ID",
            ),
        ),
    ]
