import random
from django.db import models
from helpers.common.basemodel import BaseModel
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Virtual_Card(BaseModel):
    
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

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Indicates whether the virtual card is active or not")
        )
    
    def card_number_generator(self,):
        unique_id = random.randint(1000000000, 9999999999)
        similar_obj_card_number = Virtual_Card.objects.filter(card_number=unique_id).exists()
        if similar_obj_card_number:
            return self.card_number_generator()
        return unique_id

    def save(self, *args, **kwargs) -> None:
        while not self.card_number:
            self.card_number = self.card_number_generator()
        super().save(*args, **kwargs)

    def generate_random_cvv(self,):
        return random.randint(1000000000, 9999999999)

    def save(self, *args, **kwargs) -> None:
        if not self.cvv:
            self.cvv = self.generate_random_cvv()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Virtual Card")
        verbose_name_plural = _("Virtual Cards")

    # def __str__(self):
    #     return self.card_name
    
    def __str__(self):
        return f"{self.card_name} ({self.card_number})"

    def save(self, *args, **kwargs):
        if not self.card_name:
            user = get_user_model().objects.get(id=1)
            self.card_name = user.full_name
        super().save(*args, **kwargs)
    

CARD_TYPE = (
    ('master Card', _('Master Card')),
    ('Verve Card', _('Verve Card')),
    ('Visa Card', _('Visa Card')),
)

class Bank_Card(BaseModel):
    
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

    expiration_date = models.DateField(
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
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    # def __str__(self):
    #     return self.card_name
    
    def __str__(self):
        return f"{self.card_name} ({self.card_number})"