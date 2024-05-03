from django.shortcuts import render
from portfolio_app.models import PortfolioItem

# Create your views here.

def portfolio_detail(request, id):
    image_det = PortfolioItem.objects.get(id = id)
    return render(request, 'portfolio-details.html', {'image_det': image_det})

