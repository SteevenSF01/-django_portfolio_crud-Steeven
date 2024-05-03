from django import forms
from hero_app.models import Hero


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['name', 'title']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'admin':
            raise forms.ValidationError('Not a valid name')
        return name