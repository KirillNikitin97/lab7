
from django.contrib import admin
from django.urls import path, include
from loginsys import views


urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('registration/', views.registration),

]