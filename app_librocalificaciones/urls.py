from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app_librocalificaciones' 

urlpatterns = [
    path('libro_calificaciones', views.libro_calificaciones, name="libro_calificaciones"),
    path('inicio', views.inicio, name="inicio"),
    path('evaluacion_lista', views.evaluacion_lista, name="evaluacion_lista"),
    path('evaluacion_crear', views.evaluacion_crear, name="evaluacion_crear"),
    path('evaluacion_editar/<int:id>', views.evaluacion_editar, name="evaluacion_editar"),
    path('evaluacion_eliminar/<int:id>', views.evaluacion_eliminar, name="evaluacion_eliminar"),
    path('actividad_nuevo', views.actividad_crear, name='actividad_crear'),  
    path('actividad_lista', views.actividad_lista, name='actividad_lista'),
    path('actividad_editar/<int:id>', views.actividad_editar, name='actividad_editar'),
    path('actividad_eliminar/<int:id>', views.actividad_eliminar, name='actividad_eliminar'),
    path('libro_calificaciones', views.libro_calificaciones, name='libro_calificaciones'),
    path('lista_libro_calificaciones', views.lista_libro_calificaciones, name='lista_libro_calificaciones'),
    path('libro_crear', views.libro_crear, name= 'libro_crear' ),
    path('eliminar_nuevo/<int:id>', views.eliminar_nuevo, name='eliminar_nuevo'),
    path('editar_nuevo/<int:id>', views.editar_nuevo, name='editar_nuevo'),
    path('LISTAR_PERIODO', views.LISTAR_PERIODO, name="LISTAR_PERIODO"),
    path('CREAR_PERIODO', views.CREAR_PERIODO, name="CREAR_PERIODO"),
    path('REGISTRAR_PERIODO/id', views.REGISTRAR_PERIODO, name="REGISTRAR_PERIODO"),
    path('ELIMINAR_PERIODO/<int:id>', views.ELIMINAR_PERIODO, name="ELIMINAR_PERIODO"),
    path('EDITAR_PERIODO/<int:id>', views.EDITAR_PERIODO, name="EDITAR_PERIODO"),

]