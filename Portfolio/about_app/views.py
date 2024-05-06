from django.shortcuts import render, redirect
from about_app.models import Profile
from about_app.forms import ProfileForm


# Create your views here.

def about_modify(request,id):
    aboutId = Profile.objects.get(id=id)
    about = Profile.objects.all()
    form = ProfileForm(request.POST or None, instance = aboutId)
    if form.is_valid():
        form.save()
        return redirect('/settings/about-modify/1')
    return render(request, 'about_modify.html', {'form': form, 'about':about})