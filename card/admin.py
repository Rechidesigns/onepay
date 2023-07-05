from django.contrib import admin
from .models import BankCard


@admin.register(BankCard)
class BankCardAdmin (admin.ModelAdmin):
    list_display = ('user','card_number','card_name', 'cvv', 'expiry_date','card_type', 'is_active')
    list_display_links = ('card_number','card_name', 'cvv','expiry_date','card_type')

