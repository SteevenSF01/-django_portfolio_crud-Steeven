from django.shortcuts import render, redirect
from testimonials_app.models import Testimonial
from testimonials_app.forms import TestimonialForm
from hero_app.models import HeroModel
from about_app.models import Profile


def testimonial_settings(request):
    testimonials = Testimonial.objects.all()
    about = Profile.objects.all()
    hero = HeroModel.objects.all()
    return render(request, 'testimonials_settings.html', {'testimonials': testimonials, 'hero':hero, 'about':about})

def testimonial_modify(request,id):
    testimonial = Testimonial.objects.get(id=id)
    form = TestimonialForm(request.POST or None,request.FILES, instance=testimonial)
    if form.is_valid():
        form.save()
        return redirect('testimonial_settings')
    return render(request, 'testimonial_modify.html', {'form': form, 'testimonial': testimonial})

def delete_testimonial(request, id):
    testimonial = Testimonial.objects.get(id=id)
    testimonial.delete()
    return redirect('/settings/testimonials_settings/')

def create_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/settings/testimonials_settings/')
    else:
        form = TestimonialForm() 
    return render(request, 'testimonial_create.html',{'form':form})