from django.shortcuts import render, redirect
from skills_app.models import Skill
from skills_app.forms import SkillFormSet, SkillForm

def skills_settings(request):
    skills = Skill.objects.all()
    formset = SkillFormSet(queryset=skills)
    if request.method == 'POST':
        formset = SkillFormSet(request.POST, queryset=skills)
        if formset.is_valid():
            formset.save()
            return redirect('/settings/skills-modify/')
    return render(request, 'skills_settings.html', {'formset': formset, 'skills':skills})

def skills_modify(request,id):
    skill = Skill.objects.get(id=id)
    form = SkillForm(request.POST or None, instance=skill)
    if form.is_valid():
        form.save()
        return redirect('/settings/skills-settings/')
    return render(request, 'skills_modify.html', {'form': form , 'skill':skill})