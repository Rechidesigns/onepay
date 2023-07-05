from datetime import date
from card.models import BankCard
from rest_framework import serializers



class BankCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankCard
        fields = ['card_number','card_name', 'cvv', 'expiry_date','card_type', 'is_active',]