from django.contrib import admin
from app_grados.models import Nivel, SubNivel, Grado, Asignatura

class NivelAdmin(admin.ModelAdmin):
    list_display = ('get_nombre_display',)
    search_fields = ('get_nombre_display', )

class SubNivelAdmin(admin.ModelAdmin):
    list_display = ('get_nombre_display',)
    search_fields = ('get_nombre_display', )

class GradoAdmin(admin.ModelAdmin):
    list_display = ('institucion', 'nombre', 'nivel', 'subnivel', 'libro_calificacion')
    search_fields = ('nombre', )

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'grado')
    search_fields = ('nombre', )

admin.site.register(Nivel, NivelAdmin)
admin.site.register(SubNivel, SubNivelAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
