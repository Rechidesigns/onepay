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
    user = models.OneToOneField(
        User, null=True, 
        on_delete=models.CASCADE
        )

    currency = models.CharField(
        max_length=50, 
        default='NGN'
        )
    
    created_at = models.DateTimeField(
        default=timezone.now, 
        null=True
        )
    
    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")


    def __str__(self):
        return self.user.__str__()


class WalletTransaction(models.Model):

    TRANSACTION_TYPES = (
        ('deposit', 'deposit'),
        ('transfer', 'transfer'),
        ('withdraw', 'withdraw'),
    )

    wallet = models.ForeignKey(
        Wallet, null=True, 
        on_delete=models.CASCADE
        )
    
    transaction_type = models.CharField(
        max_length=200, 
        null=True,  
        choices=TRANSACTION_TYPES
        )
    
    amount = models.DecimalField(
        max_digits=100, 
        null=True, 
        decimal_places=2
        )
    
    timestamp = models.DateTimeField(
        default=timezone.now, 
        null=True
        )
    
    status = models.CharField(
        max_length=100, 
        default="pending"
        )
    
    paystack_payment_reference = models.CharField(
        max_length=100, 
        default='', 
        blank=True
        )
    
    class Meta:
        verbose_name = _("Wallet Transactions")
        verbose_name_plural = _("Wallet Transactions")

    def __str__(self):
        return self.wallet.user.__str__()
    