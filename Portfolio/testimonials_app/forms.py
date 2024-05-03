from django import forms
from testimonials_app.models import Testimonial


class HeroForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content', 'client_name', 'client_position']
        widgets = {
            'image' : forms.FileInput()
        }