from django import forms
from testimonials_app.models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content', 'client_name', 'client_position', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }



