from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.


class Country( models.Model ):
    """
    this holds the country record and information 
    which includes the iso code 2 , phone code ......
    """

    # region Fields
    name = models.CharField(
        max_length=255,
        verbose_name=_('Country Name'),
        help_text=_('English name of country'))
 
    phone_code = models.CharField(
        max_length=100,
        blank=True, null=True,
        verbose_name=_('Phone Code'),
        help_text=_('Countries International dialing phone code.'))
 
    currency = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name=_('Currency'),
        help_text=_('Official country currency.'))
 
    iso2 = models.CharField(
        max_length=2,
        blank=True, null=True,
        verbose_name=_('ISO2'),
        help_text=_('Two-letter country code'))
  
    native = models.CharField(
        max_length=255,
        blank=True, null=True,
        help_text=_('Localized or native language of country.'))
 
    created_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Created Date'),
        help_text=_('Timestamp when the record was created'))
 
    modified_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Modified Date'),
        help_text=_('Timestamp when the record was modified.'))
 
    # endregion

     # region Methods
    def __str__(self):
        return str(self.name)
    # endregion
 
    # region Metadata
    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        db_table = 'countries'
    # endregion





class State (models.Model):
    """ this hold the record for country province """
    # country province fields 
    country = models.ForeignKey(
        Country , on_delete=models.SET_NULL,
        null=True ,
        help_text = """ this holds the record for the country which the province belongs to """
    )

    province = models.CharField(
        verbose_name=_('province or state '),
        max_length= 40,
        null= True , 
        blank=True,
        help_text=""" this is the name of the province"""
    )

    active = models.BooleanField(
        default=False,
        verbose_name=_('Active'),
        help_text=_('Indicate if province is active or not'))


    created_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Created Date'),
        help_text=_('Timestamp when the record was created'))
 
    modified_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Modified Date'),
        help_text=_('Timestamp when the record was modified.'))
    
    # end country provience fields

    def __str__(self):
        return str(self.province)

    # country provience Metadata
    class Meta:
        verbose_name = _("Country Province or State ")
        verbose_name_plural = _("Country Province or State ")
        db_table = 'countries_province_or_state'
    # end country province