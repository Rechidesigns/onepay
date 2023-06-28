from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import Account_Creation
from rest_framework import status
from onepay.users.api.serializers import UserSerializer
# from .serializers import ChangePasswordSerializer
from rest_framework import generics
from django.contrib.auth.models import User




class Register_Account ( CreateAPIView ) :
    
    """
    this is the endpoint for account creation , which includes 
    the landlord and tenant information
    """
    permission_classes = [ AllowAny, ]
    serializer_class = Account_Creation

    def post (self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )

        if serializer.is_valid():
            serializer.save(request)
            # return response
            return Response( {'status':'successful', 'message':'your account is created succesfully', 'data':serializer.data } , status = status.HTTP_201_CREATED )

        return Response( {'status':'error', 'message':'check your input and try again',} , status = status.HTTP_400_BAD_REQUEST )
