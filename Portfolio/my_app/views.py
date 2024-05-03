from django.shortcuts import render
from hero_app import views
from hero_app.models import HeroModel
from about_app.models import Profile


# Create your views here.

def home(request):
    hero = HeroModel.objects.all()
    about = Profile.objects.all()
    return render(request, 'index.html', {
        'hero': hero,
        'about': about,
    })


def settings(request):
    return render(request, 'settings.html')
