from django.contrib import admin
from app_usuarios.models import Docente, Estudiante, Representante

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'identificacion', 'fecha_nacimiento', 'correo_institucional')
    search_fields = ('nombres', 'apellidos', 'identificacion')

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'identificacion', 'fecha_nacimiento', 'correo_institucional')
    search_fields = ('nombres', 'apellidos', 'identificacion')

class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'identificacion', 'fecha_nacimiento', 'correo_personal')
    search_fields = ('nombres', 'apellidos', 'identificacion')

admin.site.register(Docente, DocenteAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Representante, RepresentanteAdmin)
