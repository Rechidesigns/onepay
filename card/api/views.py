from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from card.models import BankCard
from .serializers import BankCardSerializer
import requests
from rest_framework import status
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView , CreateAPIView, UpdateAPIView, DestroyAPIView



class BankCardView(ListCreateAPIView):
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            serializer.save( user = self.request.user )
            return Response({'status': 'successful', 'message': 'You have added a Bank Card successfully', 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get ( self, request , *args, **kwargs ):
        qs = BankCard.objects.filter( user = self.request.user )
        serializer = BankCardSerializer(qs , many = True)
        return Response( {'status':'successful', 'message':'Bank Cards has been fetched successfully','data':serializer.data } , status=status.HTTP_201_CREATED )
    