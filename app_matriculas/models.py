from django.db import models
from app_ofertaacademica.models import Aniolectivo, Paralelo
from app_usuarios.models import Estudiante

class Matricula(models.Model):

    aniolectivo = models.ForeignKey(Aniolectivo, on_delete=models.CASCADE)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    paralelo=models.ForeignKey(Paralelo, on_delete=models.CASCADE, related_name="matriculas")
   
    def __str__(self):
        return str(self.estudiante)+ " - " + str(self.paralelo)

    def get_calificacion_final(self, distributivo):
        from app_calificaciones.models import Calificacionfinal
        return Calificacionfinal.objects.filter(
            matricula=self, 
            distributivo= distributivo, 
            libro_calificacion=self.paralelo.grado.libro_calificacion).first()

    def get_calificacion_periodo(self, distributivo, periodo_academico):
        from app_calificaciones.models import Calificacionperiodo
        return Calificacionperiodo.objects.filter(
            calificacion_final__matricula=self,
            calificacion_final__distributivo=distributivo,
            periodo_academico=periodo_academico).first()

    def get_calificacion_evaluacion(self, distributivo, evaluacion):
        from app_calificaciones.models import Calificacionevaluacion
        return Calificacionevaluacion.objects.filter(
            calificacion_periodo__calificacion_final__matricula=self,
            calificacion_periodo__calificacion_final__distributivo=distributivo,
            evaluacion=evaluacion).first()

    def get_calificacion_actividad(self, distributivo, actividad):
        from app_calificaciones.models import Calificacionactividad
        return Calificacionactividad.objects.filter(
            calificacion_evaluacion__calificacion_periodo__calificacion_final__matricula=self,
            calificacion_evaluacion__calificacion_periodo__calificacion_final__distributivo=distributivo,
            actividad=actividad).first()

    #hacer un metodo que se recupere la nota de promedio de calificación final utilizando filter
    def recuperar_nota_calificacionfinal(self, distributivo):
        calificacion_final = self.get_calificacion_final(distributivo)
        if calificacion_final:
            return calificacion_final.nota if calificacion_final.nota is not None else ''
        return ''

    #hacer un metodo que se recupere la nota de promedio utilizando filter
    def recuperar_nota_periodo(self, distributivo, periodo_academico):
        calificacion_periodo = self.get_calificacion_periodo(distributivo, periodo_academico)
        if calificacion_periodo:
            return calificacion_periodo.nota if calificacion_periodo.nota is not None else ''
        return ''
    
     #hacer un metodo que se recupere la nota de evaluacion utilizando filter
    def recuperar_nota_evaluacion(self, distributivo, evaluacion):
        calificacion_evaluacion = self.get_calificacion_evaluacion(distributivo, evaluacion)
        if calificacion_evaluacion:
            return calificacion_evaluacion.nota if calificacion_evaluacion.nota is not None else ''
        return ''

    #hacer un metodo que se recupere la nota de actividad utilizando filter
    def recuperar_nota_actividad(self, distributivo, actividad):
        calificacion_actividad = self.get_calificacion_actividad(distributivo, actividad)
        if calificacion_actividad:
            return calificacion_actividad.nota if calificacion_actividad.nota is not None else ''
        return ''

    def guardar_nota_actividad(self, distributivo, actividad, nota):
        calificacion_actividad = self.get_calificacion_actividad(distributivo, actividad)
        if calificacion_actividad:
            calificacion_actividad.nota = nota
            calificacion_actividad.save()
    

    def generar_calificacion_final(self, distributivo):
        from app_calificaciones.models import Calificacionfinal, Calificacionperiodo 
        from app_calificaciones.models import Calificacionevaluacion, Calificacionactividad

        # Verificar que este asignado al grado un libro de calificaciones
        libro_calificacion = self.paralelo.grado.libro_calificacion
        if libro_calificacion is not None:
            
            # Guardo Calificacionfinal
            calificacion_final = self.get_calificacion_final(distributivo)
            if calificacion_final is None:
                calificacion_final = Calificacionfinal()
                calificacion_final.matricula = self
                calificacion_final.distributivo = distributivo
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

    
   
   