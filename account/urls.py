from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("signup/", views.signup_request, name="signup"),
    path("logout/", views.logout_request, name="logout"),
    path("password/", views.password_request, name="password"),
]
