from wallet.models import Wallet, WalletTransaction, Beneficiary
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

    def get_balance(self, obj) -> str:
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



class WalletTransactionsSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = WalletTransaction
        fields = ["reference", "type", "amount","description", "status", "created_date"]

    def get_user(self, obj) -> str:
        return {
            "name": obj.wallet.user.full_name,
            "wallet_id": obj.wallet.wallet_id,

        }





class BeneficiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Beneficiary
        fields = ["id", "name", "account_number", "bank_name"]
