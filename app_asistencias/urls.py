from django.urls import path
from . import views

app_name = 'app_asistencias'

urlpatterns = [
    path('paralelos/', views.view_home, name="paralelos"),  # Lista de paralelos
    path('paralelos/<int:paralelo_id>/asistencias/', views.listar_asistencias, name="asistencias_paralelo"),  # Ver historial
    path('paralelos/<int:paralelo_id>/tomar-lista/', views.tomar_lista, name="tomar_lista"),  # Mostrar formulario
    path('paralelos/<int:paralelo_id>/registrar/', views.registrar_asistencias, name="registrar_asistencias"),  # Procesar formulario
    path('asistencias/actualizar/<int:asistencia_id>/', views.actualizar_asistencia, name="actualizar_asistencia"),  # Actualizar estado de la asistencia
]
