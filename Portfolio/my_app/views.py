from django.shortcuts import render, redirect
from hero_app import views
from hero_app.models import HeroModel
from about_app.models import Profile
from skills_app.models import Skill
from portfolio_app.models import PortfolioItem
from services_app.models import Service
from testimonials_app.models import Testimonial


# Create your views here.

def home(request):
    hero = HeroModel.objects.all()
    about = Profile.objects.all()
    skills = Skill.objects.all()
    portfolio = PortfolioItem.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {
        'hero': hero,
        'about': about,
        'skills' : skills,
        'portfolio' : portfolio,
        'services' : services,
        'testimonials' : testimonials,
    })


def settings(request):
    hero = HeroModel.objects.all()
    about = Profile.objects.all()
    return render(request, 'settings.html', {
        'hero': hero,
        'about' : about
    })
