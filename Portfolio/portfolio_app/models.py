from django.db import models

# Create your models here.

class PortfolioItem(models.Model):
    choix_categorie = (
        ('App', 'App'),
        ('Card', 'Card'),
        ('Web', 'Web'),
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=10, choices=choix_categorie)