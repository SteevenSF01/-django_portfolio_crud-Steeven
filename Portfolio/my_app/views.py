from django.shortcuts import render
from hero_app import views


# Create your views here.

def home(request):
    hero_content = views.hero_section(request)
    return render(request, 'index.html', {
        'hero_content' : hero_content,
    })
    
def login(request):
    return render(request, 'login.html')