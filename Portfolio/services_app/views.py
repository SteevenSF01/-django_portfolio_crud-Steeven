from django.shortcuts import render, redirect
from services_app.models import Service
from services_app.forms import  serviceForm
from hero_app.models import HeroModel
from about_app.models import Profile


# Create your views here.

def services_settings(request):
    services = Service.objects.all()
    about = Profile.objects.all()
    hero = HeroModel.objects.all()
    return render(request, 'services_settings.html', {'services':services, 'hero':hero, 'about':about})

def services_modify(request,id):
    services = Service.objects.get(id=id)
    form = serviceForm(request.POST or None, instance=services)
    if form.is_valid():
        form.save()
        return redirect('services_settings')
    return render(request, 'services_modify.html', {'form': form , 'services':services})

def delete_services(request, id):
    testimonial = Service.objects.get(id=id)
    testimonial.delete()
    return redirect('services_settings')

def create_services(request):
    if request.method == 'POST':
        form = serviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services_settings')
    else:
        form = serviceForm() 
    return render(request, 'services_create.html',{'form':form})