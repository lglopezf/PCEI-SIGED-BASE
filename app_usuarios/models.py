from django.db import models

class Persona(models.Model):  
    nombres = models.CharField(max_length=200)  
    apellidos = models.CharField(max_length=200)  
    identificacion = models.CharField(max_length=200, verbose_name="Identificación")  
    fecha_nacimiento = models.DateField()  

    class Meta:  
        abstract = True

    def __str__(self):  
        return self.nombres+ " " + self.apellidos

class Docente(Persona):  
    correo_institucional = models.CharField(max_length=200)  
    celular = models.CharField(max_length=15)  
    direccion = models.TextField(verbose_name="Dirección")
    
    def __str__(self):  
        return self.nombres+ " " + self.apellidos

class Estudiante(Persona): 
    correo_institucional = models.CharField(max_length=200)     

    def __str__(self):  
        return self.nombres+ " " + self.apellidos

class Representante(Persona):  
    correo_personal = models.CharField(max_length=200)   
    celular = models.CharField(max_length=15)  
    direccion = models.TextField(verbose_name="Dirección")  

    def __str__(self):  
        return self.nombres+ " " + self.apellidos
