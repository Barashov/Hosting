from django import forms
from .models import Sites

class CreateSiteForm(forms.ModelForm):
    
    class Meta:
        model = Sites
        fields = ("name", 'description', 'site_photo', 'html_file')

