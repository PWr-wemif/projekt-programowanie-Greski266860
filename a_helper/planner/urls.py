from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:longitude>&<int:latitude>/", views.planner_site, name="planner_site")
]