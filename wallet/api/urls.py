from django.urls import path
from . import views 

urlpatterns = [
    path('wallet_info/', views.WalletInfo.as_view(), name = 'wallet_info'),
    path('deposit/', views.DepositFunds.as_view(), name = 'deposit'),
    path('deposit/verify/<str:reference>/', views.VerifyDeposit.as_view(), name='verify_deposit'),
    path('transactions/', views.TransactionsView.as_view(), name="transactions"),
    path('beneficiaries/', views.BeneficiaryListCreateView.as_view(), name='beneficiary-list-create'),
    path('beneficiaries/<int:id>/', views.BeneficiaryRetrieveUpdateDestroyView.as_view(), name='beneficiary-retrieve-update-destroy'),
    path('users/<uuid:user_id>/payment-requests/', views.PaymentRequestListCreateView.as_view(), name='payment-request-list-create'),
    path('payment-requests/<int:id>/', views.PaymentRequestRetrieveUpdateDestroyView.as_view(), name='payment-request-retrieve-update-destroy'),

]



