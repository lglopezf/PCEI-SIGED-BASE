from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_ofertaacademica' 

urlpatterns = [
    path('oferta_academica', views.oferta_academica, name="oferta_academica"),

    path('admin_aniolectivo', views.admin_aniolectivo, name="admin_aniolectivo"),  
    path('aniolectivo/create', views.create_aniolectivo, name="create_aniolectivo"),  
    path('aniolectivo/update/<int:pk>/', views.update_aniolectivo, name="update_aniolectivo"),  
    path('aniolectivo/delete/<int:pk>/', views.delete_aniolectivo, name="delete_aniolectivo"),

    path('admin_paralelo', views.admin_paralelo, name="admin_paralelo"),
    path('paralelo/create', views.create_paralelo, name="create_paralelo"),
    path('paralelo/<int:pk>/update', views.update_paralelo, name="update_paralelo"),
    path('paralelo/<int:pk>/delete', views.delete_paralelo, name="delete_paralelo"),

    path('admin_distributivo', views.admin_distributivo, name= "admin_distributivo"),
    path('distributivo/create', views.create_distributivo, name="create_distributivo"),
    path('distributivo/<int:pk>/update', views.update_distributivo, name="update_distributivo"),
    path('distributivo/<int:pk>/delete', views.delete_distributivo, name="delete_distributivo"),
]