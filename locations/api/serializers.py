from rest_framework import serializers
from locations.models import Country , State


class Country_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('name', 'id',)


class States_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = ('province','id',)