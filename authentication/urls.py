from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.home, name="home"),
     path('Register', views.Register, name="Register"),
     path('Login', views.Login, name="Login"),
     path('Logout', views.Logout, name="Logout"),
    
]

