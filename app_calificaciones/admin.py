from django.contrib import admin
from app_calificaciones.models import Calificacionfinal
from app_calificaciones.models import Calificacionperiodo
from app_calificaciones.models import Calificacionevaluacion
from app_calificaciones.models import Calificacionactividad

class CalificacionfinalAdmin(admin.ModelAdmin):
    list_display = ('nota','matricula','distributivo', 'libro_calificacion')
    list_filter = ("libro_calificacion",)

class CalificacionperiodoAdmin(admin.ModelAdmin):
    list_display = ('nota', 'calificacion_final', 'periodo_academico')
    list_filter = ("periodo_academico",)

class CalificacionevaluacionAdmin(admin.ModelAdmin):
    list_display = ('nota','calificacion_periodo', 'evaluacion')
    list_filter = ("evaluacion__periodo_academico",)

class CalificacionactividadAdmin(admin.ModelAdmin):
    list_display = ('nota','calificacion_evaluacion', 'actividad')
    list_filter = ("actividad__evaluacion__periodo_academico",)

admin.site.register(Calificacionfinal, CalificacionfinalAdmin)
admin.site.register(Calificacionperiodo,CalificacionperiodoAdmin)
admin.site.register(Calificacionevaluacion,CalificacionevaluacionAdmin)
admin.site.register(Calificacionactividad,CalificacionactividadAdmin)
