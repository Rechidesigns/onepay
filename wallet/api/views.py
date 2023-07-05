from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from wallet.models import Wallet, WalletTransaction, Beneficiary
from .serializers import WalletSerializer, DepositSerializer, WalletTransactionsSerializer, BeneficiarySerializer
import requests
from rest_framework import status
from rest_framework import serializers, generics
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView , CreateAPIView, UpdateAPIView, DestroyAPIView


class WalletInfo(APIView):

    serializer_class = WalletSerializer

    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        data = WalletSerializer(wallet).data
        return Response(data)


    
class DepositFunds(CreateAPIView):

    serializer_class = DepositSerializer

    def post(self, request):
        serializer = DepositSerializer(
            data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        resp = serializer.save()
        return Response({'status':'successful','message':'Your deposit was successful','data':serializer.data }, status = status.HTTP_200_OK )
    

class VerifyDeposit(APIView):

    serializer_class = DepositSerializer

    def get(self, request, reference):
        transaction = WalletTransaction.objects.get(
        paystack_payment_reference=reference, wallet__user=request.user)
        reference = transaction.paystack_payment_reference
        url = 'https://api.paystack.co/transaction/verify/{}'.format(reference)
        headers = {
            {"authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
        }
        r = requests.get(url, headers=headers)
        resp = r.json()
        if resp['data']['status'] == 'success':
            status = resp['data']['status']
            amount = resp['data']['amount']
            WalletTransaction.objects.filter(paystack_payment_reference=reference).update(status=status,amount=amount)
            return Response( {'status':'successful', 'message':' Your transaction was made successful'} , status = status.HTTP_201_CREATED )

        return Response( status = status.HTTP_400_BAD_REQUEST)



class TransactionsView(APIView):

    serializer_class = WalletTransactionsSerializer

    def get (self, request ):
        user = request.user
        transactions = WalletTransaction.objects.filter(wallet = user.wallet)
        serializer = self.serializer_class(transactions, many = True)
        return Response({'status':'successful','message':'all transactions are fetched successfully','data':serializer.data }, status = status.HTTP_200_OK )


class BeneficiaryListCreateView(ListCreateAPIView):
    serializer_class = BeneficiarySerializer
    queryset = Beneficiary.objects.all()

class BeneficiaryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = BeneficiarySerializer
    queryset = Beneficiary.objects.all()
    lookup_field = "id"