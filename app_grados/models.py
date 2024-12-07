from django.db import models
from app_configuracion.models import Institucion
from app_librocalificaciones.models import Librocalificacion

class Nivel(models.Model):
    CHOICE_NIVEL = [
        ('inicial', 'Inicial'),
        ('EGB', 'Educación General Básica'),
        ('bachillerato', 'Bachillerato'),
    ]

    nombre = models.CharField(max_length=50, choices=CHOICE_NIVEL)

    def __str__(self):
        return self.get_nombre_display()

class SubNivel(models.Model):
    CHOICE_SUBNIVEL = [
        ('preparatoria', 'Preparatoria'),
        ('basica_elemental', 'Básica Elemental'),
        ('basica_media', 'Básica Media'),
        ('basica_superior', 'Básica Superior'),
    ]

    nombre = models.CharField(max_length=50, choices=CHOICE_SUBNIVEL)

    def __str__(self):
        return self.get_nombre_display()


class Grado(models.Model):
    nombre= models.CharField(max_length=50)
    institucion=models.ForeignKey(Institucion, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    subnivel = models.ForeignKey(SubNivel, on_delete=models.CASCADE, null=True, blank=True)
    libro_calificacion=models.ForeignKey(Librocalificacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre 

class Asignatura(models.Model):
    nombre= models.CharField(max_length=50)
    grado=models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.grado) + ' - ' + self.nombre
