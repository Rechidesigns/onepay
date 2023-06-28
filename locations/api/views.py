from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from .serializers import Country_Serializer , States_Serializer
from locations.models import Country , State

class Country_View ( ListAPIView ):
    permission_classes = [ AllowAny, ]
    serializer_class = Country_Serializer

    def get(self, request, *args, **kwargs):
        qs = Country.objects.all()
        serializer = self.serializer_class(qs , many = True)

        return Response( {'status':'successful', 'message':'this consists of all the country that is available on the database' , 'data':serializer.data }, status = status.HTTP_200_OK)



class State_View ( ListAPIView ):
    permission_classes = [ AllowAny, ]
    serializer_class = States_Serializer

    def get(  self, request,*args, **kwargs ):
        country_id = kwargs.get('country_id', None)
        try:
            country = Country.objects.get( id = country_id )
            pass
        except Exception:
            return Response( {'status':'error', 'message':'the country id is not available on the database' ,  }, status = status.HTTP_404_NOT_FOUND)
        
        qs = State.objects.filter( country__id = country_id )
        serializer = self.serializer_class(qs , many = True)
        return Response( {'status':'successful', 'message':f'this consists of all the states that is associated to the given country { country.name } ' , 'data':serializer.data }, status = status.HTTP_200_OK)