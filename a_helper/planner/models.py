from pyexpat import model
from django.db import models
from django.conf import settings
# Create your models here.
class A_object(models.Model):
    name = models.CharField(max_length=50)
    short_info = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name
    def getShortInfo(self):
        return self.short_info
    def getImage(self):
        return self.image
    
class Telescope(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    tel_type = models.CharField(max_length=50)
    aperture = models.FloatField()
    focal_length = models.PositiveIntegerField()
    max_magnitude = models.FloatField(default=0)

    def __str__(self):
        return self.name
    def getBrand(self):
        return self.brand
    def getType(self):
        return self.tel_type
    def getAperture(self):
        return self.aperture
    def getFocalLength(self):
        return self.focal_length
    def getMaxMagnitude(self):
        return self.max_magnitude
    
class Eyepiece(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    ep_type = models.CharField(max_length=50)
    field_of_view = models.PositiveIntegerField()
    focal_length = models.FloatField()

    def __str__(self):
        return self.name
    def getBrand(self):
        return self.brand
    def getType(self):
        return self.ep_type
    def getFieldOfView(self):
        return self.field_of_view
    def getFocalLength(self):
        return self.focal_length

