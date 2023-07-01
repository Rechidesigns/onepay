from django.db import models
from helpers.common.basemodel import BaseModel
from onepay.users.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _
import random
from django.core.mail import send_mail
from django.utils import timezone

# Create your models here.


class Wallet(BaseModel):
    user = models.ForeignKey(
        User, null=True, 
        on_delete=models.CASCADE,
        verbose_name= _("Wallet"),
        help_text= _("Wallet information/ID")
        )

    currency = models.CharField(
        max_length=50, 
        default='NGN',
        verbose_name= _("Currency"),
        help_text= _("The type of currency the wallet will operate on")

        )
    
    created_at = models.DateTimeField(
        default=timezone.now, 
        null=True,
        verbose_name= _("Time Created"),
        help_text= _("The time and date the card was created")
        )
    
    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")


    def __str__(self):
        return self.user



TRANSACTION_TYPES = (

        ('deposit', _('deposit')),
        ('transfer', _('transfer')),
        ('withdraw', _('withdraw')),
    )


class WalletTransaction(models.Model):

    wallet = models.ForeignKey(
        Wallet, null=True, 
        on_delete=models.CASCADE,
        verbose_name= _("Time Created"),
        help_text= _("The time and date the card was created")
        )
    
    transaction_type = models.CharField(
        max_length=200, 
        null=True,  
        choices=TRANSACTION_TYPES,
        verbose_name= _("Time Created"),
        help_text= _("The time and date the card was created")
        )
    
    amount = models.DecimalField(
        max_digits=100, 
        null=True, 
        decimal_places=2,
        verbose_name= _("Time Created"),
        help_text= _("The time and date the card was created")
        )
    
    timestamp = models.DateTimeField(
        default=timezone.now, 
        null=True,
        verbose_name= _("Time Created"),
        help_text= _("The time and date the card was created")
        )
    
    status = models.CharField(
        max_length=100, 
        default="pending",
        verbose_name= _("Time Created"),
        help_text= _("The time and date the card was created")
        )
    
    paystack_payment_reference = models.CharField(
        max_length=100, 
        default='', 
        blank=True,
        verbose_name= _("Time Created"),
        help_text= _("The time and date the card was created")
        )
    
    class Meta:
        verbose_name = _("Wallet Transactions")
        verbose_name_plural = _("Wallet Transactions")

    def __str__(self):
        return str(self.wallet)

    