from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_calificaciones' 

urlpatterns = [
    path('calificaciones', views.calificaciones, name="calificaciones"),
]