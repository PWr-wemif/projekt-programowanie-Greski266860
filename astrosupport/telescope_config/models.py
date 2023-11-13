from pyexpat import model
from django.db import models
from django.conf import settings

# Create your models here.
class Telescope(models.Model):
    name = models.CharField(max_length=100)
    tel_type = models.CharField(max_length=50)
    aperture = models.FloatField()
    focal_length = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Eyepiece(models.Model):
    name = models.CharField(max_length=100)
    ep_type = models.CharField(max_length=50)
    field_of_view = models.PositiveIntegerField()
    focal_length = models.FloatField()

    def __str__(self):
        return self.name