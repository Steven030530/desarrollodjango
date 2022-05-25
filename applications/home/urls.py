from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('prueba/',views.PruebaView.as_view()),
    path('lista/',views.PruebaListView.as_view()),
    path('listado/',views.PruebaListado.as_view()),
    path('Add/',views.PruebaCreateView.as_view()),
    path("generalhome/",views.VistaGeneralHome.as_view()),
    path("inicio/",views.Inicio.as_view()),
    path("resumen_f/",views.ResumenFoundationView.as_view())

    
]
