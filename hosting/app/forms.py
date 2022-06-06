from django import forms
from .models import Sites

class CreateSiteForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field',
                                                         'placeholder': 'название сайта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'field',
                                                               'placeholder': 'описание'}))
    site_photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control file-input',
                                                                'id': 'file'}))
    html_file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.html',
                                                              'class': 'form-control file-input',
                                                              'id': 'html_file'}))
    
    class Meta:
        model = Sites
        fields = ("name", 'description', 'site_photo', 'html_file')

