from django.db import models

# Create your models here.

class PortfolioItem(models.Model):
    choix_categorie = (
        ('app', 'app'),
        ('card', 'card'),
        ('web', 'web'),
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=10, choices=choix_categorie)