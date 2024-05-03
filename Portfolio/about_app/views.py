from django.shortcuts import render, redirect
from about_app.models import Profile
from about_app.forms import ProfileForm


# Create your views here.

def about_modify(request,id):
    about = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None, instance = about)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'about_modify.html', {'form': form})