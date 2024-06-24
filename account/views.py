from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def login_request(request):
        if request.user.is_authenticated:
          return redirect("index")
        if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login (request, user)
               return redirect("index")
          else:
               return render(request, "account/login.html", {"error":"Kullanıcı adı veya şifre hatalı"})
        return render(request, "account/login.html")



def password_request(request):
        return render(request, "account/password.html")


def signup_request(request):
        if request.user.is_authenticated:
          return redirect("index")
        if request.method == "POST":
          username = request.POST["username"]
          email = request.POST["email"]
          firstname = request.POST["firstname"]
          lastname = request.POST["lastname"]
          password = request.POST["password"]
          repassword = request.POST["repassword"]
          
          if password == repassword:
               if User.objects.filter(username=username).exists():
                    return render(request, "account/register.html", {"error":"Kullanıcı adı kullanılıyor"})
               else:
                    if User.objects.filter(email=email).exists():
                         return render(request, "account/register.html", {"error":"Email kullanılıyor"})
                    else:
                         user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
                         user.save()
                         return redirect("login")
          else:
               return render(request, "account/register.html", {"error":"Şifreler uyuşmuyor"})
           
        return render(request, "account/signup.html")
   
def logout_request(request):
     return redirect("index")