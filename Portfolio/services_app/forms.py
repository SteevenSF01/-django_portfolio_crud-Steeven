from django import forms
from services_app.models import Service
from django.forms import modelformset_factory

class serviceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ("title","icon","description")

servicesFormSet = modelformset_factory(Service, form=serviceForm, extra=0)