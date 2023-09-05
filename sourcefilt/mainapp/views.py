from django.shortcuts import render


# Create your views here.

def index(request):
     return render(request, "mainapp/index.html")

def about(request):
    return render(request, "mainapp/about.html")

def source(request):
     return render(request, "mainapp/source.html")

def sndhand(request):
    return render(request, "mainapp/sndhand.html")