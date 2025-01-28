from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_matriculas' 

urlpatterns = [
    path('matriculas', views.matriculas, name="matriculas"),
    path('matriculados_lista/', views.matriculados_lista, name="matriculados_lista"),
    path('matriculas_crear/', views.matriculas_crear, name="matriculas_crear"),
    path('matriculas_editar/<int:id>/', views.matriculas_editar, name="matriculas_editar"),
    path('matriculas_eliminar/<int:id>/', views.matriculas_eliminar, name="matriculas_eliminar"),
]