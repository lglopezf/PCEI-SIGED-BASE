from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app_librocalificaciones' 

urlpatterns = [

    path('libro_calificaciones', views.inicio, name="libro_calificaciones"), 
    
    path('libro_calificacion_lista', views.libro_lista, name='libro_lista'),
    path('libro_calificacion_crear', views.libro_crear, name= 'libro_crear' ),
    path('libro_calificacion_editar/<int:id>', views.libro_editar, name='libro_editar'),
    path('libro_calificacion_eliminar/<int:id>', views.libro_eliminar, name='libro_eliminar'),

    path('PERIODO_LISTA', views.PERIODO_LISTA, name="PERIODO_LISTA"),
    path('PERIODO_CREAR', views.PERIODO_CREAR, name="PERIODO_CREAR"),
    path('PERIODO_EDITAR/<int:id>', views.PERIODO_EDITAR, name="PERIODO_EDITAR"),
    path('PERIODO_ELIMINAR/<int:id>', views.PERIODO_ELIMINAR, name="PERIODO_ELIMINAR"),

    path('evaluacion_lista', views.evaluacion_lista, name="evaluacion_lista"),
    path('evaluacion_crear', views.evaluacion_crear, name="evaluacion_crear"),
    path('evaluacion_editar/<int:id>', views.evaluacion_editar, name="evaluacion_editar"),
    path('evaluacion_eliminar/<int:id>', views.evaluacion_eliminar, name="evaluacion_eliminar"),
    
    path('actividad_lista', views.actividad_lista, name='actividad_lista'),
    path('actividad_nuevo', views.actividad_crear, name='actividad_crear'),  
    path('actividad_editar/<int:id>', views.actividad_editar, name='actividad_editar'),
    path('actividad_eliminar/<int:id>', views.actividad_eliminar, name='actividad_eliminar'),
    
]