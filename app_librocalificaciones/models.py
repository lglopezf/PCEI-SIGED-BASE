from django.db import models

class Librocalificacion(models.Model):

    CHOICE_CALCULO_TOTAL=(
    ('ponderado', 'Ponderado'),
    ('promedio_simple', 'Promedio simple'),
    )
    
    nombre=models.CharField(max_length=50, choices=CHOICE_CALCULO_TOTAL, unique=True)
    
    def __str__(self):
        return self.get_nombre_display()

class Periodoacademico(models.Model):
    nombre=models.CharField(max_length=50) 
    orden=models.PositiveIntegerField() 
    librocalificacion=models.ForeignKey(Librocalificacion,on_delete=models.CASCADE, related_name='periodos_academicos')

    def __str__(self):
        return str(self.librocalificacion) + ' - ' + self.nombre

class Evaluacion(models.Model):

    CHOICE_NOMBRE=(
    ('evalucion_sumativa', 'Evaluación sumativa'),
    ('evaluacion_formativa', 'Evaluación formativa'),
    )

    nombre=models.CharField(max_length=50, choices=CHOICE_NOMBRE)
    ponderado=models.IntegerField(null=True, blank=True)
    periodo_academico=models.ForeignKey(Periodoacademico, on_delete=models.CASCADE, related_name='evaluaciones')

    def __str__(self):
        if self.ponderado:
            return str(self.periodo_academico) + ' - ' + self.get_nombre_display() + ' - Ponderado: ' + str(self.ponderado)
        return str(self.periodo_academico) + ' - ' + self.get_nombre_display()

class Actividad(models.Model):
    CHOICE_TIPO=(
    ('actividad_grupal', 'Actividad grupal'),
    ('actividad_individual', 'Actividad individual'),
    ('leccion', 'Lección'),
    ('evalucion_final', 'Evaluación Final'),
    )

    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50, choices=CHOICE_TIPO)
    evaluacion=models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='actividades')

    def __str__(self):
        return str(self.evaluacion) + ' - ' + self.get_tipo_display() + ' - ' + self.nombre
