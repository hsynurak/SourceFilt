from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("source/", views.source, name="source"),
]

