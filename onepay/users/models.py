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

    wallet_id = models.CharField(
        blank=True, null=True,
        max_length=10, 
        unique=True)

    pin = models.CharField(
        max_length=4,
        default='0000',
        help_text=_("The PIN of the customer.")
    )

    def save(self, *args, **kwargs):
        if not self.wallet_id:
            self.wallet_id = self.generate_wallet_id()

        super(User, self).save(*args, **kwargs)

    def generate_wallet_id(self):
        wallet_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        return wallet_id


    def send_account_creation_email(self):
        subject = "OnePay Account Created"
        message = f"Dear {self.first_name},\n\nYour OnePay account has been created successfully!\n\nAccount Number: {self.wallet_id}\n\n Quickly complete the KYC section so you can enjoy the full benefits of OnePay. Thank you for joining OnePay!"
        send_mail(subject, message, None, [self.email])

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

