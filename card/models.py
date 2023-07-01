from django.db import models
from helpers.common.basemodel import BaseModel
# Create your models here.
from django.utils.translation import gettext_lazy as _


class Card(BaseModel):
    
    card_number = models.IntegerField(
        max_length=16, 
        null= True,
        blank= True,
        verbose_name= _("cards"),
        help_text= _("Card number")
    )

    month = models.IntegerField(
        max_length=2, 
        null= True,
        blank= True,
        verbose_name= _("month"),
        help_text= _("Card ecperiry month")
    )

    year = models.IntegerField(
        max_length=4, 
        null= True,
        blank= True,
        verbose_name= _("year"),
        help_text= _("Card expiry year")
    )

    card_name = models.CharField(
        max_length= 200,
        null= True,
        blank= True,
        verbose_name= _("Card Name"),
        help_text= _("Card holder name")
        )
    
    cvv =models.IntegerField(
        max_length=3, 
        null= True,
        blank= True,
        verbose_name= _("CVV"),
        help_text= _("Card Verification Value")
    )

    
    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    # def __str__(self):
    #     return self.card_name
    
    def __str__(self):
        return f"{self.card_name} ({self.card_number})"