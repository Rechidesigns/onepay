#  import DRF packages
from rest_framework import serializers

#  import Django packages
from django.contrib.auth import get_user_model

#  import Recuity packages
from kyc.models import KycApplication
from locations.api.serializers import Country_Serializer , States_Serializer




class Kyc_Serializer(serializers.ModelSerializer):

    class Meta:
        model = KycApplication
        exclude = [ 'kyc_submitted_ip_address','registered_ip_address','user','reviewer', 'kyc_review_date','reviewer_ip_address','kyc_refused_code', ]

    def create(self, validated_data):
        # Perform any additional processing or custom logic before saving the KycApplication instance

        # Example: Set the KYC status based on some condition
        if validated_data.get('some_field') == 'some_value':
            validated_data['kyc_status'] = 'approved'
        else:
            validated_data['kyc_status'] = 'pending'

        # Save the KycApplication instance
        kyc_application = KycApplication.objects.create(**validated_data)

        # Perform any other custom logic or data manipulation if needed

        return kyc_application


class KYC_GET_Serializer (serializers.ModelSerializer):
    country = Country_Serializer( read_only = True )
    state = States_Serializer( read_only = True )
    nationality = Country_Serializer( read_only = True )
    second_citizenship = Country_Serializer( read_only = True )
    country_residence = Country_Serializer( read_only = True )

    class Meta:
        model = KycApplication
        exclude = ['user', 'reviewer']
