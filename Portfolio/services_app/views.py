from django.shortcuts import render, redirect
from services_app.models import Service
from services_app.forms import servicesFormSet

# Create your views here.

def services_modify(request):
    services = Service.objects.all()
    formset = servicesFormSet(queryset=services)
    if request.method =='POST':
        formset = servicesFormSet(request.POST, queryset=services)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    return render(request, 'services_modify.html', {'formset': formset})