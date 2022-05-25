from django.contrib import admin
from django.urls import path
from . import views



app_name = 'departamento_app'
def Appdepartamento(self):
    print("===============HOLA DEPARTAMENTO===============")


urlpatterns = [
    path("departamento/",Appdepartamento),
    path("registro_dpto/",views.NewRegisterDpto.as_view()),
    path("lista_dpto",views.ListDpto.as_view(),name="lista_depa"),
    
]
