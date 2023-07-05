from django.urls import path
from . import views 

urlpatterns = [
    path('bank-card/' , views.BankCardView.as_view() , name = "bankcard_view"),
]
