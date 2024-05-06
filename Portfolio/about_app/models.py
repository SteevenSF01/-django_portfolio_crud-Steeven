from django.db import models

# Create your models here.


class Profile(models.Model):
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.BooleanField()   
    image = models.ImageField(upload_to='images/', default='images/default.png')