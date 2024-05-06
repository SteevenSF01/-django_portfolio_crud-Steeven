from django.shortcuts import render, redirect
from hero_app.models import HeroModel
from hero_app.forms import HeroForm

# Create your views here.
def modify_hero(request, id):
    hero = HeroModel.objects.get(id=id)
    heroAll = HeroModel.objects.all()
    form = HeroForm(request.POST or None, instance=hero)
    if form.is_valid():
        form.save()
        return redirect('/settings/modify_hero/1')
    return render(request, 'modify_hero.html', {'form':form, 'heroall':heroAll})