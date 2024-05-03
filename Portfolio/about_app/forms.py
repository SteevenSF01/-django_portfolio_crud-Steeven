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

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['birthday'].widget.attrs.update({'class': 'form-control'})
        self.fields['website'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['degree'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['freelance'].widget.attrs.update({'class': 'form-control'})