from django.db import models
from app_ofertaacademica.models import Aniolectivo, Paralelo
from app_usuarios.models import Estudiante

class Matricula(models.Model):

    aniolectivo = models.ForeignKey(Aniolectivo, on_delete=models.CASCADE)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    paralelo=models.ForeignKey(Paralelo, on_delete=models.CASCADE)
   
    def __str__(self):
        return str(self.estudiante)+ " - " + str(self.paralelo)

    def get_calificacion_final(self, distributivo):
        from app_calificaciones.models import Calificacionfinal
        return Calificacionfinal.objects.filter(
            matricula=self, 
            distributivo= distributivo, 
            libro_calificacion=self.paralelo.grado.libro_calificacion).first()
