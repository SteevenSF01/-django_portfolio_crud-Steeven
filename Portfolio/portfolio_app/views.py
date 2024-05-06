from django.shortcuts import render, redirect
from portfolio_app.models import PortfolioItem
from portfolio_app.forms import portfolioForm
from hero_app.models import HeroModel
from about_app.models import Profile


# Create your views here.

def portfolio_detail(request, id):
    image_det = PortfolioItem.objects.get(id = id)
    return render(request, 'portfolio-details.html', {'image_det': image_det})

def portfolio_settings(request):
    portfolio = PortfolioItem.objects.all()
    about = Profile.objects.all()
    hero = HeroModel.objects.all()
    return render(request, 'portfolio_settings.html', {'portfolio':portfolio ,'about': about, 'hero':hero})


def portfolio_modify(request,id):
    portfolio = PortfolioItem.objects.get(id=id)
    form = portfolioForm(request.POST, request.FILES or None, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('portfolio_settings')
    return render(request, 'portfolio_modify.html', {'form': form , 'portfolio':portfolio})

def delete_portfolio(request, id):
    testimonial = PortfolioItem.objects.get(id=id)
    testimonial.delete()
    return redirect('portfolio_settings')

def create_portfolio(request):
    if request.method == 'POST':
        form = portfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio_settings')
    else:
        form = portfolioForm() 
    return render(request, 'portfolio_create.html',{'form':form})