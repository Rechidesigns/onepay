import random
from django.db import models
from helpers.common.basemodel import BaseModel
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from onepay.users.models import User



CARD_TYPE = (
    ('master Card', _('Master Card')),
    ('Verve Card', _('Verve Card')),
    ('Visa Card', _('Visa Card')),
)

class BankCard(BaseModel):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name= _("Card Owner"),
        help_text= _("ID of the card holder")
    )

    card_number = models.CharField(
        max_length=16,
        verbose_name=_("Card Number"),
        help_text=_("The card number of the virtual card")
    )

    card_name = models.CharField(
        max_length= 200,
        null= True,
        blank= True,
        verbose_name= _("Card Name"),
        help_text= _("Card holder name")
        )
    
    cvv =models.CharField(
        max_length=3,
        verbose_name= _("CVV"),
        help_text= _("Card Verification Value")
        )

    expiry_date = models.CharField(
        max_length=4,
        verbose_name=_("Expiration Date"),
        help_text=_("The expiration date of the virtual card")
        )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Indicates whether the virtual card is active or not")
        )
    
    card_type = models.CharField(
        max_length= 20,
        choices= CARD_TYPE,
        verbose_name= _("Card Type"),
        help_text= _("Card type of the virtual card")
    )
    
    class Meta:
        verbose_name = _("Bank Card")
        verbose_name_plural = _("Bank Cards")



    # def __str__(self):
    #     return self.card_name
    
    def __str__(self):
        return f"{self.card_name} ({self.card_number})"