from django.shortcuts import render, redirect

# Create your views here.

from .forms import SkillForm

def create_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings/')
    else:
        form = SkillForm()
    
    return render(request, 'modify_skills.html', {'form': form})
