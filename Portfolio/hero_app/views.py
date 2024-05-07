from django.shortcuts import render, redirect
from hero_app.models import HeroModel
from hero_app.forms import HeroForm
from hero_app.models import HeroModel
from about_app.models import Profile


# Create your views here.
def modify_hero(request, id):
    hero = HeroModel.objects.all()
    hero2 = HeroModel.objects.get(id=id)
    about = Profile.objects.all()
    heroAll = HeroModel.objects.all()

    form = HeroForm(request.POST or None, instance=hero2)
    if form.is_valid():
        form.save()
        return redirect('/settings/modify_hero/1')
    return render(request, 'modify_hero.html', {'form':form, 'hero':hero,'heroAll':heroAll, 'about':about})