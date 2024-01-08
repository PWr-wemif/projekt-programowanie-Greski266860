from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:latitude>/<int:longitude>/", views.a_label, name="a_label")
]