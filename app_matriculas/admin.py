from django.contrib import admin

from app_matriculas.models import Matricula

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aniolectivo', 'estudiante', 'paralelo')


admin.site.register(Matricula, MatriculaAdmin)
