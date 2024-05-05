from django.shortcuts import render, redirect
from testimonials_app.models import Testimonial
from testimonials_app.forms import TestimonialForm
from django.forms import formset_factory

def testimonial_settings(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials_settings.html', {'testimonials': testimonials})

def testimonial_modify(request,id):
    testimonial = Testimonial.objects.get(id=id)
    form = TestimonialForm(request.POST or None, instance=testimonial)
    if form.is_valid():
        form.save()
        return redirect('testimonial_settings')
    return render(request, 'testimonial_modify.html', {'form': form})