from django.contrib import admin
from kyc.models import KycApplication

@admin.register(KycApplication)
class KycApplicationAdmin (admin.ModelAdmin):
    list_display = ('legal_first_names', 'legal_last_names', 'birth_date', 'email', 'address_line_1', 'address_line_2', 'state', 'zip_code',
                     'city', 'identification_type','address_proof_type','proof_of_address_document', 'photo_id', 'photo_id_back', 'selfie_with_id',
                     'kyc_status', 'kyc_status_note','status_update_date','politically_exposed_person', 'place_of_birth','date_of_birth','identification_number',
                     'identification_issue_date', 'identification_expiry', 'kyc_submitted_ip_address','registered_ip_address','accept_terms',
                     'agreed_to_data_usage','citizenship','second_citizenship','country_residence','user','reviewer', 'kyc_review_date','reviewer_ip_address',
                     'kyc_refused_code')
    list_display_links = ('legal_first_names', 'legal_last_names', 'user')