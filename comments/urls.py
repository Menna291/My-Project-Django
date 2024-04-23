from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.add_comment, name='comments'),
    path('comments', views.show_comments, name='show_comments'),
    
    
    
]
