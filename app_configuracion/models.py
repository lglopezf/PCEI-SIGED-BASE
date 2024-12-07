from django.db import models

# Create your models here.
class Institucion(models.Model):

    CHOICE_SOSTENIMIENTO = (("fiscal", "Fiscal"),
                         ("particular", "Particular"),
                         ("municipal", "Municipal"),
                         ("fiscomisional", "Fiscomisional"))

    CHOICE_MODALIDAD = (("presencial", "Presencial"),
                         ("semipresencial", "Semipresencial"),
                         ("distancia", "Distancia"),
                         ("enlinea", "En línea"))
    
    nombre = models.CharField(max_length=200)
    sostenimiento = models.CharField(choices=CHOICE_SOSTENIMIENTO, max_length=50)
    modalidad = models.CharField(choices=CHOICE_MODALIDAD, max_length=50)

    def __str__(self):
        return self.nombre
