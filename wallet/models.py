from django.db import models
from helpers.common.basemodel import BaseModel
from onepay.users.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _
import random
from django.core.mail import send_mail
from django.utils import timezone

# Create your models here.
from django.utils.crypto import get_random_string

class Wallet(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name= _("User Wallet"),
        help_text= _("The type of currency the wallet will operate on")
        )

    wallet_id = models.CharField(
        max_length=10, 
        unique=True,
        verbose_name= _("Wallet ID"),
        help_text= _("The wallet ID of the user which serves as a the account number of the wallet")
        )

    pin = models.CharField(
        max_length=4,
        default='0000',
        verbose_name= _("Card Pin"),
        help_text=_("The PIN of the customer.")
        )

    currency = models.CharField(
        max_length=50, 
        default='NGN',
        verbose_name= _("Currency"),
        help_text= _("The type of currency the wallet will operate on")
        )
    
    
    def wallet_id_generator(self,):
        unique_id = random.randint(1000000000, 9999999999)
        similar_obj_wallet_id = Wallet.objects.filter(wallet_id=unique_id).exists()
        if similar_obj_wallet_id:
            return self.wallet_id_generator()
        return unique_id

    def save(self, *args, **kwargs) -> None:
        while not self.wallet_id:
            self.wallet_id = self.wallet_id_generator()
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")


    def __str__(self):
        return str(self.user)



TRANSACTION_TYPES = (

        ('deposit', _('deposit')),
        ('transfer', _('transfer')),
        ('withdraw', _('withdraw')),
    )


class WalletTransaction(BaseModel):

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        verbose_name= _("Wallet Transaction"),
        help_text= _("The wallet ID of the transaction")
        )
    
    type = models.CharField(
        max_length=200,   
        choices=TRANSACTION_TYPES,
        verbose_name= _("Type"),
        help_text= _("The type of ctransaction performed")
        )
    
    amount = models.DecimalField(
        max_digits=100, 
        decimal_places=2,
        verbose_name= _("Amount"),
        help_text= _("The amount of the transaction in figures")
        )
    
    status = models.CharField(
        max_length=15, 
        default="pending",
        verbose_name= _("Status"),
        help_text= _("The status of the transaction")
        )
    
    reference = models.CharField(
        max_length=50,
        verbose_name= _("Transaction Reference"),
        help_text= _("The holds the reference of the transactions")
        )
    
    def generate_transaction_reference(self):
        unique_code = get_random_string(15)
        similar_wallet = WalletTransaction.objects.filter(reference = unique_code).exists()
        if similar_wallet:
            return self.generate_transaction_reference()
        return unique_code

    def save(self, *args, **kwargs) -> None:
        while not self.reference:
            self.reference = self.generate_transaction_reference()
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = _("Wallet Transactions")
        verbose_name_plural = _("Wallet Transactions")

    def __str__(self):
        return str(self.wallet)

    