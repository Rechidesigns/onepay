from wallet.models import Wallet, WalletTransaction
from rest_framework import serializers
from django.db.models import Sum
from django.contrib.auth.models import User
from django.conf import settings
import requests

class WalletSerializer(serializers.ModelSerializer):
    """
    Serializers to validate the user's wallet 
    """
    balance = serializers.SerializerMethodField()

    def get_balance(self, obj):
        bal = WalletTransaction.objects.filter(
            wallet=obj, status="success").aggregate(Sum('amount'))['amount__sum']
        return bal

    class Meta:
        model = Wallet
        fields = ['wallet_id', 'currency', 'balance']


def is_amount(value):
    if value <= 0:
        raise serializers.ValidationError({"detail": "Invalid Amount"})
    return value



class DepositSerializer(serializers.Serializer):

    amount = serializers.IntegerField(validators=[is_amount])
    email = serializers.EmailField()

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            return value
        raise serializers.ValidationError({"detail": "Email not found"})

    # def save(self):
    #     user = self.context['request'].user
    #     wallet = Wallet.objects.get(user=user)
    #     data = self.validated_data
    #     WalletTransaction.objects.create(
    #         wallet=wallet,
    #         transaction_type="deposit",
    #         amount= data["amount"],
    #         status="pending",
    #     )



class WalletTransactionsSerializer(serializers.Serializer):
        
    user = serializers.SerializerMethodField()
    reference = serializers.CharField(read_only=True)
    type = serializers.CharField()
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    status = serializers.CharField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True,)

    def get_user(self, obj):
        return {
            "name": obj.wallet.user.full_name,
            "wallet_id": obj.wallet.wallet_id,

        }

