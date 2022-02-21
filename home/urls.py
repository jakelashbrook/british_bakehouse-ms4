from django.contrib import admin
from django.contrib.auth.urls import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
