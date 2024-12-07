from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_configuracion' 

urlpatterns = [
    path('institucion', views.institucion, name="institucion"),
    path('institucion_crear', views.institucion_crear, name="institucion_crear"),
    path('institucion_editar/<int:id>', views.institucion_editar, name="institucion_editar"),
    path('institucion_eliminar/<int:id>', views.institucion_eliminar, name="institucion_eliminar"),
]