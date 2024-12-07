from django.contrib import admin
from app_librocalificaciones.models import Librocalificacion, Periodoacademico, Evaluacion, Actividad

class LibrocalificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    search_fields =('nombre',)

class PeriodoacademicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'librocalificacion')
    search_fields =('nombre',)
    list_filter = ("librocalificacion",)

class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ponderado', 'periodo_academico')
    search_fields =('nombre',)
    list_filter = ("periodo_academico",)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'evaluacion')
    search_fields =('nombre',)
    list_filter = ("evaluacion__periodo_academico",)


admin.site.register(Librocalificacion,LibrocalificacionAdmin)
admin.site.register(Periodoacademico,PeriodoacademicoAdmin)
admin.site.register(Evaluacion,EvaluacionAdmin,)
admin.site.register(Actividad,ActividadAdmin,)
