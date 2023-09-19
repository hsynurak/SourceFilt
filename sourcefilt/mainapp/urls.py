from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("index", views.index),
     path("about", views.about, name="about"),
     path("source", views.source, name="source"),
     path("sndhand", views.sndhand, name="sndhand"),
     path("details", views.details, name="details"),
     path("contact", views.contact, name="contact"),
]
