from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_calificaciones' 

urlpatterns = [
    path('calificaciones', views.calificaciones, name="calificaciones"),
    path('verlibro/<int:id>', views.verlibro, name="verlibro"),
    path('verevaluaciones/<int:iddistributivo>/<int:idperiodoacademico>', views.verevaluaciones, name="verevaluaciones"),
    path('ingresarnotas/<int:iddistributivo>/<int:idactividades>', views.ingresarnotas, name="ingresarnotas"),
    path('guardarnotas/<int:iddistributivo>/<int:idactividades>', views.guardarnotas, name="guardarnotas"),
    path('calcularpromedio_calificacionfinal/<int:iddistributivo>', views.calcularpromedio_calificacionfinal, name="calcularpromedio_calificacionfinal"),
    path('calcularpromedios_periodo_evaluaciones/<int:iddistributivo>/<int:idperiodoacademico>', views.calcularpromedios_periodo_evaluaciones, name="calcularpromedios_periodo_evaluaciones"),
]