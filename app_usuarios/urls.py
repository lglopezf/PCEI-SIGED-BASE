from django.contrib import admin
from django.urls import path
from app_usuarios import views

app_name = "app_usuarios"

urlpatterns = [
    path('usuarios', views.usuarios, name="usuarios"),
    path('docentes', views.admin_docentes, name="admin_docentes"),  
    path('docentes/create', views.create_docente, name="create_docente"),  
    path('docentes/<int:pk>/update', views.update_docente, name="update_docente"),  
    path('docentes/<int:pk>/delete', views.delete_docente, name="delete_docente"),  

    path('estudiantes', views.admin_estudiantes, name='admin_estudiantes'),  
    path('estudiantes/create', views.create_estudiante, name='create_estudiante'),  
    path('estudiantes/<int:pk>/update', views.update_estudiante, name='update_estudiante'),  
    path('estudiantes/<int:pk>/delete', views.delete_estudiante, name='delete_estudiante'),  

    path('representantes', views.admin_representantes, name='admin_representantes'),  
    path('representantes/create', views.create_representante, name='create_representante'),  
    path('representantes/<int:pk>/update', views.update_representante, name='update_representante'),  
    path('representantes/<int:pk>/delete', views.delete_representante, name='delete_representante'),
]