from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class signupform(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password1','password2']

class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=('user',)
