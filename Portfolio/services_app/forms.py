from django import forms
from services_app.models import Service

class Form(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ("title","icon","description")
