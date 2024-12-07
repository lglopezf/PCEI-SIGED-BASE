from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_grados' 

urlpatterns = [
    path('grados', views.grados, name="grados"),
]