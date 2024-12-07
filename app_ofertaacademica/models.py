from django.db import models
from app_grados.models import Grado, Asignatura
from app_usuarios.models import Docente


class Aniolectivo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

    def get_distributivos(self):
        return self.distributivos.all()


class Paralelo(models.Model):
    nombre = models.CharField(max_length=50)
    grado=models.ForeignKey(Grado, on_delete=models.CASCADE)
    aniolectivo = models.ForeignKey(Aniolectivo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.aniolectivo) + ' - ' + str(self.grado) + ' - ' + self.nombre

class Distributivo(models.Model):
    aniolectivo = models.ForeignKey(Aniolectivo, on_delete=models.CASCADE, related_name='distributivos')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    paralelo = models.ForeignKey(Paralelo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.aniolectivo) + " - " + str(self.asignatura)+ " - " + str(self.docente)+ " - " + str(self.paralelo.nombre)

    def get_matriculas(self):
        from app_matriculas.models import Matricula
        return Matricula.objects.filter(paralelo=self.paralelo)

    def generar_libro_calificaciones(self):
        from app_calificaciones.models import Calificacionfinal, Calificacionperiodo 
        from app_calificaciones.models import Calificacionevaluacion, Calificacionactividad

        # Verificar que este asignado al grado un libro de calificaciones
        libro_calificacion = self.paralelo.grado.libro_calificacion
        if libro_calificacion is not None:
            
            # Genero por cada matrícula
            matriculas = self.get_matriculas()
            for matricula in matriculas:
                
                # Guardo Calificacionfinal
                calificacion_final = matricula.get_calificacion_final(self)
                if calificacion_final is None:
                    calificacion_final = Calificacionfinal()
                    calificacion_final.matricula = matricula
                    calificacion_final.distributivo = self
                    calificacion_final.libro_calificacion = libro_calificacion
                    calificacion_final.save()

                # Guardo Calificacionperiodo
                for periodo_academico in libro_calificacion.periodos_academicos.all():
                    
                    calificacion_periodo = Calificacionperiodo.objects.filter(
                        calificacion_final=calificacion_final, 
                        periodo_academico=periodo_academico).first()
                    
                    if calificacion_periodo is None:
                        calificacion_periodo = Calificacionperiodo()
                        calificacion_periodo.calificacion_final = calificacion_final
                        calificacion_periodo.periodo_academico = periodo_academico
                        calificacion_periodo.save()

                    # Guardo Calificacionevaluacion
                    for evaluacion in periodo_academico.evaluaciones.all():

                        calificacion_evaluacion = Calificacionevaluacion.objects.filter(
                            calificacion_periodo=calificacion_periodo, 
                            evaluacion=evaluacion).first()

                        if calificacion_evaluacion is None:
                            calificacion_evaluacion = Calificacionevaluacion()
                            calificacion_evaluacion.calificacion_periodo = calificacion_periodo
                            calificacion_evaluacion.evaluacion = evaluacion
                            calificacion_evaluacion.save()

                        # Guardo Calificacionactividad
                        for actividad in evaluacion.actividades.all():

                            calificacion_actividad = Calificacionactividad.objects.filter(
                                calificacion_evaluacion=calificacion_evaluacion, 
                                actividad=actividad).first()

                            if calificacion_actividad is None:
                                calificacion_actividad = Calificacionactividad()
                                calificacion_actividad.calificacion_evaluacion = calificacion_evaluacion
                                calificacion_actividad.actividad = actividad
                                calificacion_actividad.save()