from django.contrib import admin
from django.urls import path, include
from lab7 import views


urlpatterns = [
    path('', views.home),
]
