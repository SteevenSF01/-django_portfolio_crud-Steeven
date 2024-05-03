from django.shortcuts import render
from hero_app import views
from hero_app.models import HeroModel
from about_app.models import Profile
from skills_app.models import Skill
from portfolio_app.models import PortfolioItem
from services_app.models import Service


# Create your views here.

def home(request):
    hero = HeroModel.objects.all()
    about = Profile.objects.all()
    skills = Skill.objects.all()
    portfolio = PortfolioItem.objects.all()
    services = Service.objects.all()
    return render(request, 'index.html', {
        'hero': hero,
        'about': about,
        'skills' : skills,
        'portfolio' : portfolio,
        'services' : services,
    })


def settings(request):
    return render(request, 'settings.html')
