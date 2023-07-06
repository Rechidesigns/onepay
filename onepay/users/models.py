import random
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from helpers.common.basemodel import BaseModel
from onepay.users.managers import UserManager
import uuid
from locations.models import Country
# import django packages
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


from django.dispatch import receiver

from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.utils import timezone
# from shortuuid.django_fields import ShortUUIDFields
# from shortuuidfield import ShortUUIDField




class User(AbstractUser):
    """
    Default custom user model for OnePay.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    KYC_STATUS = (
        ('unverified', _('Unverified')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action_required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected/Refused'))
    )


    objects = UserManager()

    #: First and last name do not cover name patterns around the globe
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )

    name = CharField(_("Name of User"), blank=True, max_length=255)

    email = models.EmailField(
        max_length=150,
        verbose_name=_("Email Address"),
        unique=True,
        help_text=_("The email address of the customer.")
    )

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    first_name = models.CharField(
        max_length=255,
        verbose_name=_("First names"),
        blank=True, null=True,
        help_text=_("The first names of the customer.")
    )

    last_name = models.CharField(
        max_length=255,
        verbose_name=_("Last names"),
        blank=True, null=True,
        help_text=_("The first names of the customer.")
    )

    contact_number = models.CharField(
        max_length=50,
        verbose_name=_("Contact Number"),
        blank=True, null=True,
        help_text=_("The contact number of the customer.")
    )
    
    # KYC section fo the user model 

    kyc_complete = models.BooleanField(
        verbose_name=_("KYC complete"),
        null=True,
        blank=True,
        default=False,
        help_text=_("Flag to determine if a cutomer have completed KYC verification")
    )

    kyc_complete_date = models.DateTimeField(
        verbose_name=_("KYC complete date"),
        blank=True,
        null=True,
        help_text=_("Timestamp when customer completed KYC verifiction process.")
    )

    kyc_status = models.CharField(
        max_length=15,
        verbose_name=_("KYC status"),
        choices=KYC_STATUS,
        default='Unverified',
        blank=True,
        null=True,
        help_text=_("The .")
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        verbose_name = _("Register User")
        verbose_name_plural = _("Registered Users")

    # def __str__(self):
    #     return str(self.email)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"email": self.pk})
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Your Recuity account"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@recuity.com",
        # to:
        [reset_password_token.user.email]
    )

