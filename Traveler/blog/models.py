from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    direccion = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=30)

def __str__(self):
    return self.nombre + ", " + self.apellido + ", " + self.telefono + ", " + self.email + self.direccion + ", " + self.region + ", " + self.contrasenia #linea nueva
