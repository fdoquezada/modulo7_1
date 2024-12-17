from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    edad = models.IntegerField()
    registro = models.DateTimeField(auto_now_add=True)
    
class curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    estudiante = models.ManyToManyField(Estudiante, related_name='cursos')
    
    def __str__(self):
            return self.nombre