
from django.utils.translation import gettext_lazy as _


class ModelChoices:


    UTILITY = "UTILITY"


    PROOF_OF_ADDRESS_TYPE = (
        (UTILITY, _("Utility Bill")),
    )

    PHOTO_IDENTIFICATION_TYPE = (
        ('national_id', _("National ID")),
        ("passport", _("Passport")),
        ("drivers_license", _("Drivers License"))

    )

    KYC_STATUS = (
        ("verified", _("verified")),
        ("unverified", _("Unverified")),
        ("pending", _("Pending")),
        ("rejected", _("Rejected")),
        ("cancelled", _("Cancelled"))
    )

    PEP_CHOICES = (
        ("pep", _("Yes, I'm politically exposed")),
        ("non_pep", _("No, I'm not politically exposed"))
    )

    KYC_REFUSE_REASON_CODE = (
        ("EXPIRED_DOCUMENT", _("Document Expired")),
        ("DOCUMENT_DOES_NOT_MATCH_USER_DATA", _("Document does not match user data"))
    )