from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_matriculas' 

urlpatterns = [
    path('matriculas', views.matriculas, name="matriculas"),
]