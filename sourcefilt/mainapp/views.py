from django.core.mail import EmailMessage
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from mainapp.models import Index_Slider, Member, Review, Category, Source, UserInfo
from .forms import ContactForm


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

def details(request):
    return render(request, "mainapp/details.html")

def contact(request):
     if request.method == "POST":
          form = ContactForm(request.POST)
          if form.is_valid():
               name = form.cleaned_data["name"]
               email = form.cleaned_data["email"]
               phone = form.cleaned_data["phone"]
               message = form.cleaned_data["message"]
               form.save()
               messages.success(request, "Mesajın başarı ile alındı.")
               return redirect("contact")
     else:
          form = ContactForm()
     return render(request, "mainapp/contact.html", {"form": form})
