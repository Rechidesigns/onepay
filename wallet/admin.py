from django.contrib import admin
from wallet.models import Wallet, WalletTransaction
# Register your models here.

@admin.register(Wallet)
class WalletAdmin (admin.ModelAdmin):
    list_display = ('user','currency', 'created_date',)
    list_display_links = ('user','currency', 'created_date',)
    readonly_fields = ("wallet_id", "pin")


@admin.register(WalletTransaction)
class WalletTransaction (admin.ModelAdmin):
    list_display = ('wallet','type', 'amount','created_date','status',)
    list_display_links = ('wallet','type', 'amount','created_date','status')
    readonly_fields =("reference",)