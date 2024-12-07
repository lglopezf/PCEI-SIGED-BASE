from django.db import models
from app_matriculas.models import Matricula
from app_ofertaacademica.models import Distributivo
from app_librocalificaciones.models import Librocalificacion, Periodoacademico, Evaluacion, Actividad

class Calificacionfinal(models.Model):

    nota = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    distributivo = models.ForeignKey(Distributivo, on_delete=models.CASCADE)
    libro_calificacion = models.ForeignKey(Librocalificacion, on_delete=models.CASCADE)

    def __str__(self):
        return '(Matrícula) ' + str(self.matricula)+ ' (Distributivo) ' + str(self.distributivo.asignatura.nombre) + ' (Nota final) ' + str(self.nota)


class Calificacionperiodo(models.Model):
    
    nota=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    calificacion_final = models.ForeignKey(Calificacionfinal, on_delete=models.CASCADE, related_name='calificacion_periodos')
    periodo_academico = models.ForeignKey(Periodoacademico, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.calificacion_final) + ' (Nota periodo) ' + str(self.nota)

class Calificacionevaluacion(models.Model):
    
    nota=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    calificacion_periodo = models.ForeignKey(Calificacionperiodo, on_delete=models.CASCADE, related_name='calificacion_evaluaciones')
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.calificacion_periodo) + ' (Nota evaluación) ' + str(self.nota)
    
class Calificacionactividad(models.Model):
   
    nota= models.DecimalField(max_digits=10, decimal_places=2, null=True)
    calificacion_evaluacion = models.ForeignKey(Calificacionevaluacion, on_delete=models.CASCADE, related_name='calificacion_actividades')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.calificacion_evaluacion) + ' (Nota actividad) ' + str(self.nota)
    
