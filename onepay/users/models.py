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



class User(AbstractUser):
    """
    Default custom user model for OnePay.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

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


    class Meta:
        verbose_name = _("Register User")
        verbose_name_plural = _("Registered Users")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"email": self.pk})
    


class Wallet(BaseModel):
    wallet_id = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return self.wallet_id



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