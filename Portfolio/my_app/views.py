from django.shortcuts import render
from hero_app import views


# Create your views here.

def home(request):
    return render(request, 'index.html', {
    })
    
def settings(request):
    return render(request, 'settings.html')