from django.contrib import admin
from app_ofertaacademica.models import Aniolectivo, Paralelo, Distributivo

class AniolectivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre', )

class ParaleloAdmin(admin.ModelAdmin):
    list_display = ('aniolectivo', 'grado', 'nombre',)
    search_fields = ('nombre', )

class DistributivoAdmin(admin.ModelAdmin):
    list_display = ('aniolectivo', 'asignatura', 'docente', 'paralelo')
    search_fields = ('nombre', )


admin.site.register(Aniolectivo, AniolectivoAdmin)
admin.site.register(Paralelo, ParaleloAdmin)
admin.site.register(Distributivo, DistributivoAdmin)