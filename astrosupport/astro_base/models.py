from pyexpat import model
from django.db import models
from django.conf import settings
# Create your models here.
class DS_object(models.Model):
    name = models.CharField(max_length=50)
    catalogue_index = models.CharField(max_length=50)
    size = models.FloatField()
    abs_brigth = models.FloatField()
    short_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def getCatalogueIndex(self):
        return self.catalogue_index
    def getSize(self):
        return self.size
    def getAbsBrigth(self):
        return self.abs_brigth
    def getShortInfo(self):
        return self.short_info

class US_object(models.Model):
    name = models.CharField(max_length=50)
    short_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def getShortInfo(self):
        return self.short_info
    