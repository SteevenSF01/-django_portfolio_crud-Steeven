from django.db import models

# Create your models here.

class HeroModel(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField()
    