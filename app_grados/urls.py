from django.contrib import admin # type: ignore
from django.urls import path  
from . import views 
 
app_name = 'app_grados'  
 
urlpatterns = [ 
    path('grados', views.grados, name="grados"),  
    path('grados_crear', views.grados_crear, name="grados_crear"), 
    path('grados_listar', views.grados_listar, name="grados_listar"), 
    path('grados_editar/<int:id>/', views.grados_editar, name="grados_editar"), 
    path('grados_eliminar/<int:id>/', views.grados_eliminar, name="grados_eliminar"), 
    path('asignaturas_crear', views.asignaturas_crear, name="asignaturas_crear"), 
    path('asignaturas_listar', views.asignaturas_listar, name="asignaturas_listar"), 
    path('asignaturas/editar/<int:id>/', views.asignaturas_editar, name='asignaturas_editar'),
    path('asignaturas_eliminar/<int:id>', views.asignaturas_eliminar, name="asignaturas_eliminar"),  

]

