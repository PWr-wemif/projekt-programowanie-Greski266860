from django.contrib import admin

# Register your models here.
from .models import A_object, Telescope, Eyepiece

admin.site.register(A_object)
admin.site.register(Telescope)
admin.site.register(Eyepiece)