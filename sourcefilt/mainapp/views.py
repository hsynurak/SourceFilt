from django.shortcuts import render

from mainapp.models import Index_Slider, Member, Review


# Create your views here.

def index(request):
     index_sliders = Index_Slider.objects.all()
     reviews = Review.objects.all()
     context = {"index_sliders": index_sliders, "reviews": reviews}
     return render(request, "mainapp/index.html",context)

def about(request):
     members = Member.objects.all()
     context = {"members": members}
     return render(request, "mainapp/about.html", context)

def source(request):
     return render(request, "mainapp/source.html")

def sndhand(request):
    return render(request, "mainapp/sndhand.html")