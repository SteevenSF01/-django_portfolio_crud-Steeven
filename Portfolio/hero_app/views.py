from django.shortcuts import render

# Create your views here.

def hero_section(request):
    return render(request, 'hero.html')