from django.contrib import admin
from django.urls import path
from . import views

def saludo(self):
    for i in range(10):
        print("DARWIN EL MEJOR DEL MUNDO")

app_name = "persona_app"

urlpatterns = [
    path("persona/",saludo),
    path("lista_empleados/",views.ListEmpleado.as_view(),name="empleados_all"),
    path("lista_area/<name>",views.ListEmpArea.as_view(),name="area_empleado"),
    path("buscar_empleado/",views.ListEmpleadosByKword.as_view()),
    path("listado_habilidades/",views.ListHabilidades.as_view()),
    path("detalle_empleado/<pk>",views.EmpleadoDetailView.as_view(),name="detalle_empleado"),
    path("agregar_persona/",views.PersonaCreateView.as_view()),
    path("success/",views.SuccessView.as_view(),name = "correcto"),
    path("editar_empleado/<pk>",views.PersonasUpdateView.as_view()),
    path("eliminar_empleado/<pk>",views.PersonasDeleteView.as_view()),
    path("",views.InicioView.as_view()),
]
