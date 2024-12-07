from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_ofertaacademica' 

urlpatterns = [
    path('oferta_academica', views.oferta_academica, name="oferta_academica"),
]