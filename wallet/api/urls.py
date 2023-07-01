from django.urls import path
# from .views import Login, Register, VerifyDeposit, WalletInfo, DepositFunds
from . import views 

urlpatterns = [
    path('wallet_info/', views.WalletInfo.as_view(), name = 'wallet_info'),
    path('deposit/', views.DepositFunds.as_view(), name = 'deposit'),
    path('deposit/verify/<str:reference>/', views.VerifyDeposit.as_view()),
    path('transactions/', views.TransactionsView.as_view())
]



