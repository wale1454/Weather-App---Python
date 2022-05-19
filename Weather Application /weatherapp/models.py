from pyexpat import model
from django.db import models

# Create your models here.

class CityName (models.Model):
    contentInside = models.CharField(max_length=250)


    def __str__(self):
        return self.contentInside