from  django import forms
from .models import Lead,LeadFile
from crispy_forms.helper import FormHelper


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
                "first_name",
                "last_name",
                "user_name",
                "firm_name",
                "firm_type",
                "PAN",
                "GST",
                "authorized_person_firstname",
                "authorized_person_lastname",
                "registered_address_of_company",
                "email_id",
                "email_id_of_autherized_person",
                "mobile_number",
                
                "password"
            
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class LeadFileModelForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = (
            'authority_letter',
            'pan_photo',
            'client_credential_file',
            'gst_document',
            'photo_of_authorized_person',
           
        )
