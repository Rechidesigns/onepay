from django.urls import path
from . import views 

urlpatterns = [
    path('add-kyc/', views.Kyc_View.as_view(), name='KYC_Application'),
    path('kyc-detail/<str:id>/', views.Kyc_Detail_View.as_view(), name='KYC_detail'),
]