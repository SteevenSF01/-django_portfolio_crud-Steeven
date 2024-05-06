from django.db import models

# Create your models here.

class Testimonial(models.Model):
    content = models.TextField()
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/default.png')