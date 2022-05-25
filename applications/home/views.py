from ast import For
from pathlib import PurePath
from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView , CreateView
from matplotlib.style import context

from applications.home.forms import PruebaForm
from .models import Prueba_Dpto
from .forms import PruebaForm
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'



class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'


class PruebaListView(ListView):
    template_name = "home/lista.html" # Ruta para ver el template html
    context_object_name = 'ListaNumeros'
    queryset = ['1','10','20','30']


class PruebaListado(ListView):
    template_name = "home/listado.html"
    model = Prueba_Dpto
    context_object_name = "list"
    

class Add(CreateView):
    template_name = "home/add.html"
    model = Prueba_Dpto
    fields = ["titulo","subtitulo","cantidad"]


class VistaGeneralHome(TemplateView):
    template_name = "home/generalhome.html"
    

class Inicio(ListView):
    template_name = "home/inicio.html"
    model = Prueba_Dpto


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba_Dpto
    form_class = PruebaForm
    success_url = "/"