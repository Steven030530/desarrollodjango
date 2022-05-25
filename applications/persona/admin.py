from django.contrib import admin
from .models import Habilidades, Personas

# Register your models here.


admin.site.register(Habilidades)



class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "first_lastname",
        "correo",
        "departamento",
        "fullname",
        "id",
    )

    def fullname(self,obj):
        return obj.first_name + " " + obj.first_lastname

    search_fields = (
        "first_name",
    )
    list_filter = ("departamento",)
    filter_horizontal = ("habilidad",)   

admin.site.register(Personas,EmpleadoAdmin)