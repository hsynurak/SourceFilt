from django.shortcuts import render

from mainapp.models import Index_Slider, Member, Review, Category, Source


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
     categories = Category.objects.all()
     sources = Source.objects.all()
     context = {"categories": categories , "sources": sources}
     return render(request, "mainapp/source.html", context)

def sndhand(request):
    return render(request, "mainapp/sndhand.html")