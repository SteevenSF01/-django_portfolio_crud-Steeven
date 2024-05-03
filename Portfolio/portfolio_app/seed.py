from django_seed import Seed
from portfolio_app.models import PortfolioItem

def runPortfolio():
    seeder = Seed.seeder()
    images_details= [
        {'title' : 'Image 1', 'image': 'img/portfolio/portfolio-1.jpg' ,'category':'app'},
        {'title' : 'Image 2', 'image': 'img/portfolio/portfolio-2.jpg' ,'category':'web'},
        {'title' : 'Image 3', 'image': 'img/portfolio/portfolio-3.jpg' ,'category':'app'},
        {'title' : 'Image 4', 'image': 'img/portfolio/portfolio-4.jpg' ,'category':'card'},
        {'title' : 'Image 5', 'image': 'img/portfolio/portfolio-5.jpg' ,'category':'web'},
        {'title' : 'Image 6', 'image': 'img/portfolio/portfolio-6.jpg' ,'category':'app'},
        {'title' : 'Image 7', 'image': 'img/portfolio/portfolio-7.jpg' ,'category':'card'},
        {'title' : 'Image 8', 'image': 'img/portfolio/portfolio-8.jpg' ,'category':'app'},
        {'title' : 'Image 9', 'image': 'img/portfolio/portfolio-9.jpg' ,'category':'web'},
    ]
    for image in images_details:
        seeder.add_entity(PortfolioItem, 1,image)
    pks = seeder.execute()
    print(pks , 'Portfolio created')