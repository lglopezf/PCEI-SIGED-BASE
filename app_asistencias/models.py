from django.db import models
from app_matriculas.models import Matricula
from app_ofertaacademica.models import Distributivo
from app_usuarios.models import Docente

class Asistencia(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    distributivo = models.ForeignKey(Distributivo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha) + '-' + str(self.hora_inicio) + '-' + str(self.hora_fin) 
