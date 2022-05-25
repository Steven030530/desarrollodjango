from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from applications.departamento.models import Departamento
from .models import Personas
from django.urls import reverse_lazy

class ListEmpleado(ListView):
    template_name = "persona/lista_empleados.html"
    model = Personas
    paginate_by = 4

    def get_queryset(self):
        print("*************************")
        palabra_clave = self.request.GET.get("kword","")
        lista = Personas.objects.filter(
            full_name__icontains=palabra_clave
        )
        print("Lista Resultado: ",lista)
        return lista

class ListEmpArea(ListView):
    ''' Listado de Empleados que pertenecen a un area'''
    template_name = "persona/lista_area.html"
    model = Personas
    #queryset = Personas.objects.filter(
        #departamento__name = "Area Contable"
    #) la peor forma de hacer el filtro

    def get_queryset(self):
        area = self.kwargs["name"]
        lista = Personas.objects.filter(
            departamento__name = area
        )
        return lista


class ListEmpleadosByKword(ListView):
    template_name = "persona/by_kword.html"
    context_object_name = "empleados"
    

    def get_queryset(self):
        print("*************************")
        palabra_clave = self.request.GET.get("kword","")
        print("=================",palabra_clave)
        lista = Personas.objects.filter(
            first_name = palabra_clave
        )
        print("Lista Resultado: ",lista)
        return lista


class ListHabilidades(ListView):
    template_name = "persona/lista_habilidad.html"
    context_object_name = "habil"

    def get_queryset(self):
        
        id = (self.request.GET.get('list',""))
        id = int(id)
        empleado = Personas.objects.get(id=int(id))


        return  empleado.habilidad.all()


class EmpleadoDetailView(DetailView):
    model = Personas
    template_name = "persona/detail_empleado.html"


    def get_context_data(self, **kwargs):
         context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
         context["titulo"] = "Empleado del Mes"
         return context



class SuccessView(TemplateView):
    template_name = "persona/success.html"



class PersonaCreateView(CreateView):
    model = Personas
    template_name = "persona/add_persona.html"
    fields = ["first_name", "first_lastname","age","correo","departamento"]
    success_url = reverse_lazy("persona_app:correcto")

    def form_valid(self,form):

        empleado = form.save()
        print(empleado)
        empleado.full_name = empleado.first_name + empleado.second_name + " " +  " " + empleado.first_lastname + " " + empleado.second_lastname
        empleado.save()
        return super(PersonaCreateView,self).form_valid(form)



class PersonasUpdateView(UpdateView):
    model = Personas
    template_name = "persona/update.html"
    fields = ("__all__")
    success_url = reverse_lazy("persona_app:correcto")



class PersonasDeleteView(DeleteView):
    model = Personas
    template_name = "persona/delete.html"
    fields = ("__all__")
    success_url= reverse_lazy("persona_app:correcto")


class InicioView(TemplateView):
    """ Vista para cargar pantalla de inicio"""
    template_name = "inicio.html"



