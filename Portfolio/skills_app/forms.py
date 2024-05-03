from django import forms
from django.forms import modelformset_factory
from skills_app.models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']

SkillFormSet = modelformset_factory(Skill, form=SkillForm, extra=0)
