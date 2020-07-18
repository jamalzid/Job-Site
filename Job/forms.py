from django import forms
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields='__all__'
        exclude=('owner','slug',)

class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields='__all__'
        exclude = ('job',)

class commentform(forms.ModelForm):
    class Meta:
        model=Comment
        firlds='__all__'
        exclude = ('published_at',)
