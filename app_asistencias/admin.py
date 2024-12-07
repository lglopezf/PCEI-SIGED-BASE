from django.contrib import admin
from app_asistencias.models import Asistencia

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora_inicio', 'hora_fin', 'matricula', 'distributivo')


admin.site.register(Asistencia, AsistenciaAdmin)
