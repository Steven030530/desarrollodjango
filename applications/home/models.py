from fileinput import filename
from django.db import models

# Create your models here.

class Prueba_Dpto(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self): 

        return self.titulo + " " + self.subtitulo + " " + str(self.cantidad)

