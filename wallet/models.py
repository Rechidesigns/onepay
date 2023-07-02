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
        help_text= _("The user detail that owns the wallet")
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

STATUS =(
    ('')
)

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



class UpComingPayment(BaseModel):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name= _("User Upcoming payment"),
        help_text= _("this holds the user scheduling the payment")
        )
    
    name = models.CharField(
        max_length= 50,
        verbose_name = _("Name"),
        help_text= _("The purpose of the payment")
        )

    status = models.CharField(
        max_length=15, 
        default="pending",
        verbose_name= _("Status"),
        help_text= _("The status of the transaction")
        )
 
    amount = models.DecimalField(
        max_digits=100, 
        decimal_places=2,
        verbose_name= _("Amount"),
        help_text= _("The amount of the transaction in figures")
        )
    
    class Meta:
        verbose_name = _("Up-Coming Payment")
        verbose_name_plural = _("Up-Coming Payments")

    def __str__(self):
        return str(self.user)


class PaymentRequest(BaseModel):

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payment_requests',
        verbose_name=_("Requester"),
        help_text=_("The user requesting the payment")
    )

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_payment_requests',
        verbose_name=_("Recipient"),
        help_text=_("The user receiving the payment request")
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Amount"),
        help_text=_("The amount requested for payment")
    )

    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Description of the payment request or invoice")
    )

    status = models.CharField(
        max_length=15, 
        default="pending",
        verbose_name= _("Status"),
        help_text= _("The status of the transaction")
        )
    

    class Meta:
        verbose_name = _("Payment Request")
        verbose_name_plural = _("Payment Requests")

    # def __str__(self):
    #     return str(self.requester)


    def __str__(self):
        return f"Payment Request #{self.id} from {self.requester.full_name} to {self.recipient.full_name}"



class Beneficiary(BaseModel):

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        verbose_name=_("Wallet"),
        help_text=_("The wallet associated with the beneficiary")
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_("Beneficiary Name"),
        help_text=_("The name of the beneficiary")
    )

    account_number = models.CharField(
        max_length=20,
        verbose_name=_("Account Number"),
        help_text=_("The account number of the beneficiary")
    )

    bank_name = models.CharField(
        max_length=100,
        verbose_name=_("Bank Name"),
        help_text=_("The name of the bank where the beneficiary's account is held")
    )

    class Meta:
        verbose_name = _("Beneficiary")
        verbose_name_plural = _("Beneficiary")

    def __str__(self):
        return str(self.name)




