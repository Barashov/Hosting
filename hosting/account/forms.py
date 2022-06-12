from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2',)
        model = User
        
        
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form',
                                                             'placeholder': 'логин'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form',
                                                                  'placeholder': 'пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form',
                                                                  'placeholder': 'повтор пароля'}))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = "Confirm Password"
        
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ("name", "surname", "profile_image", "bio", "email")
