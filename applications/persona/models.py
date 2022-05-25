from pyexpat import model
from django.db import models
from joblib import MemorizedResult
from sklearn.feature_extraction import img_to_graph
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad",max_length=50)


    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades Empleados"

    def __str__(self):
        return  str(self.id) + " " + self.habilidad
 


class Personas(models.Model):

    job_choices = (
        ("0","Contador"),
        ("1","Adminitrador"),
        ("2","Economista"),
        ("3","Otro")
        )

    first_name = models.CharField("Primer Nombre", max_length=50)
    second_name = models.CharField("Segundo Nombre", max_length=50, blank=True)
    first_lastname = models.CharField("Primer Apellido",max_length=50)
    second_lastname = models.CharField("Segundo Apellido",max_length=50, blank=True)
    full_name = models.CharField(
        "Nombres Completos",
        max_length=200,
        blank=True
        )
    age = models.IntegerField("Edad",blank=True)
    correo = models.EmailField("Correo Electronico")
    job = models.CharField("Trabajo",max_length=50,choices=job_choices,blank=True)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE,blank=True)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidad = models.ManyToManyField(Habilidades,blank=True)
    hoja_vida = RichTextField(blank=True)

    class Meta:
        verbose_name = "Empleados"
        verbose_name_plural = "Empleado"
        ordering = ["first_lastname"]

    def __str__(self):
        return  str(self.id) + " " +self.first_name + " " + self.first_lastname 


