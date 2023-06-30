from django.contrib import admin
from wallet.models import Wallet, WalletTransaction
# Register your models here.

@admin.register(Wallet)
class WalletAdmin (admin.ModelAdmin):
    list_display = ('user','currency', 'created_at',)
    list_display_links = ('user','currency', 'created_at',)


@admin.register(WalletTransaction)
class WalletTransaction (admin.ModelAdmin):
    list_display = ('wallet','transaction_type', 'amount','timestamp','status','paystack_payment_reference')
    list_display_links = ('wallet','transaction_type', 'amount','timestamp','status')