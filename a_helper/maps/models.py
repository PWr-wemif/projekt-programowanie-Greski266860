from django.db import models

# Create your models here.
class Localization(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()