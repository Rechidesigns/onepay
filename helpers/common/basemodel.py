import uuid 
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel (models.Model):
    id = models.UUIDField(
        verbose_name = _('id'),
        default = uuid.uuid4,
        editable = False,
        primary_key = True,
        help_text = _('this is the unique identifier of an object')
    )

    created_date = models.DateTimeField(
        verbose_name=_("Created Date"),
        default=timezone.now,
        help_text=_("Timestamp when the record was created.")
        )

    modified_date = models.DateTimeField(
        verbose_name=_("Modified Date"),
        # default=timezone.now,
        auto_now=True,
        help_text=_("Modified date when the record was created.")
        )

    #Metadata
    class Meta :
        abstract = True


    # def __str__(self):
    #     return self.created_date




