from django.contrib import admin
from .models import Virtual_Card, Bank_Card

@admin.register(Virtual_Card)
class Virtual_CardAdmin (admin.ModelAdmin):
    list_display = ('card_number','card_name', 'cvv','created_date','is_active')
    list_display_links = ('card_number','card_name', 'cvv','created_date')
    

@admin.register(Bank_Card)
class Bank_CardAdmin (admin.ModelAdmin):
    list_display = ('card_number','card_name', 'cvv', 'expiration_date','card_type', 'is_active')
    list_display_links = ('card_number','card_name', 'cvv','expiration_date','card_type')
    