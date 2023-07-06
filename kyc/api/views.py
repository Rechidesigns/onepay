# import DRF packages 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import  CreateAPIView,RetrieveUpdateDestroyAPIView

# import Django packages 
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.exceptions import ValidationError

# import Recuity App packages 
from .serializers import Kyc_Serializer , KYC_GET_Serializer
from kyc.models import KycApplication
from onepay.users.models import User



# class Kyc_View(CreateAPIView):

#     serializer_class = Kyc_Serializer
#     queryset = KycApplication.objects.none()

#     def post(self, request, *args, **kwargs):
#         user_info = User.objects.get(id=self.request.user.id)

#         if user_info.kyc_complete:
#             raise ValidationError("You have already submitted a KYC!")

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=self.request.user)

#             # updating the user kyc object
    
#             user_info.kyc_complete = True
#             user_info.kyc_complete_date = timezone.now()
#             user_info.save()
#             # updating user kyc ends here 

#             return Response({'status': 'successful', 'message': 'KYC has been uploaded successfully', 'data': serializer.data},
#                             status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Kyc_View(CreateAPIView):
    serializer_class = Kyc_Serializer
    queryset = KycApplication.objects.none()

    def post(self, request, *args, **kwargs):
        user = self.request.user

        if user.kyc_complete:
            raise ValidationError("You have already submitted a KYC!")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            kyc_application = serializer.save(user=user)

            # Update the user's KYC status and other fields
            user.kyc_complete = True
            user.kyc_complete_date = timezone.now()
            user.save()
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"status": "success", "message": "KYC application submitted successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )

    
    def get ( self, request , *args, **kwargs ):
        qs = KycApplication.objects.filter( user = self.request.user )
        serializer = KYC_GET_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'Kyc details has been fetched','data':serializer.data } , status=status.HTTP_200_OK )




class Kyc_Detail_View( RetrieveUpdateDestroyAPIView ): 

    serializer_class = KYC_GET_Serializer
    queryset = KycApplication.objects.all()
    lookup_field = "id"