from django.shortcuts import render, redirect
from skills_app.models import Skill
from skills_app.forms import SkillFormSet

def skills_modify(request):
    skills = Skill.objects.all()
    formset = SkillFormSet(queryset=skills)
    if request.method == 'POST':
        formset = SkillFormSet(request.POST, queryset=skills)
        if formset.is_valid():
            formset.save()
            return redirect('')
    return render(request, 'skills_modify.html', {'formset': formset})