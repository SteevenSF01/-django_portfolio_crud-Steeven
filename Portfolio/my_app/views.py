from django.shortcuts import render
from hero_app import views
from hero_app.models import HeroModel


# Create your views here.

def home(request):
    hero = HeroModel.objects.all()
    return render(request, 'index.html', {
        'hero':hero
    })
    
def settings(request):
    return render(request, 'settings.html')