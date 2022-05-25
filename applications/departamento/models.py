from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField("Nombre",max_length=50)
    shor_name = models.CharField("Nombre corto", max_length=20)
    anulate = models.BooleanField("Anulado",default=False)
    
    class Meta:
        verbose_name = "Mi Departamento"
        verbose_name_plural = "Areas de mi Empresa"

    def __str__(self):
        return str(self.id) + "-" + self.name + "-" + self.shor_name



