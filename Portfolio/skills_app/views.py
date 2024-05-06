from django.shortcuts import render, redirect
from skills_app.models import Skill
from skills_app.forms import SkillFormSet, SkillForm
from hero_app.models import HeroModel
from about_app.models import Profile

# Create your views here.

def skills_settings(request):
    skills = Skill.objects.all()
    hero = HeroModel.objects.all()
    about = Profile.objects.all()

    formset = SkillFormSet(queryset=skills)
    if request.method == 'POST':
        formset = SkillFormSet(request.POST, queryset=skills)
        if formset.is_valid():
            formset.save()
            return redirect('/settings/skills-modify/')
    return render(request, 'skills_settings.html', {'formset': formset, 'skills':skills,'hero': hero,
        'about' : about
})

def skills_modify(request,id):
    skill = Skill.objects.get(id=id)
    form = SkillForm(request.POST or None, instance=skill)
    if form.is_valid():
        form.save()
        return redirect('/settings/skills-settings/')
    return render(request, 'skills_modify.html', {'form': form , 'skill':skill})

def delete_skill(request, id):
    testimonial = Skill.objects.get(id=id)
    testimonial.delete()
    return redirect('/settings/skills-settings/')

def create_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/settings/skills-settings/')
    else:
        form = SkillForm() 
    return render(request, 'skill_create.html',{'form':form})