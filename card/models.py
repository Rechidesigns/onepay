from django.db import models
from helpers.common.basemodel import BaseModel
# Create your models here.
from django.utils.translation import gettext_lazy as _


class VirtualCard(BaseModel):
    
    card_number = models.CharField(
        max_length=16,
        verbose_name=_("Card Number"),
        help_text=_("The card number of the virtual card")
    )
    
    cvv = models.CharField(
        max_length=4,
        verbose_name=_("CVV"),
        help_text=_("The CVV of the virtual card")
    )

    card_name = models.CharField(
        max_length= 200,
        null= True,
        blank= True,
        verbose_name= _("Card Name"),
        help_text= _("Card holder name")
        )
    
    cvv =models.IntegerField(
        verbose_name= _("CVV"),
        help_text= _("Card Verification Value")
    )

    expiration_date = models.DateField(
        verbose_name=_("Expiration Date"),
        help_text=_("The expiration date of the virtual card")
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Indicates whether the virtual card is active or not")
    )
    
    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    # def __str__(self):
    #     return self.card_name
    
    def __str__(self):
        return f"{self.card_name} ({self.card_number})"