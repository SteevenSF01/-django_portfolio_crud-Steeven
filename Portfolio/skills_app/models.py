from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=0, help_text='Max 100')