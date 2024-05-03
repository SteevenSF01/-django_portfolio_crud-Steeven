from django import forms
from skills_app.models import Skill

class skillsForm(forms.ModelForm):
    class Meta:
        model = Skill
        field = ['name','proficiency']