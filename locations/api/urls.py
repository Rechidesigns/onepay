from django.urls import path
from . import views 

urlpatterns = [
    path('all-country/', views.Country_View.as_view() , name = 'all-country'),
    path('states/<str:country_id>/' , views.State_View.as_view() , name = "all_states"),
]


