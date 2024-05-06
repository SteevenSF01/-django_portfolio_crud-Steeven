from django import forms
from about_app.models import Profile
from django.db import models

# Create your models here.

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'birthday',
            'website',
            'phone',
            'city',
            'age',
            'degree',
            'email',
            'freelance',
        ]
        widget = {
            'birthday' : forms.DateInput(attrs={'class': 'form-group', 'type':'date'})
        }
