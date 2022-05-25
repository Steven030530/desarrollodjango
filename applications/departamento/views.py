from django.views.generic import ListView
from django.shortcuts import render

from .forms import NewDepartamentoForm
from django.views.generic.edit import FormView
from applications.persona.models import Personas
from .models import Departamento

class NewRegisterDpto(FormView):
    template_name = 'departamento/new_register.html'
    form_class = NewDepartamentoForm
    success_url = "/admin"

    def form_validate(self, form):
        #print("++++++++++++++++estamos en el form_validate+++++++++++++++++++++++++++")
        

        depa = Departamento(
            name = form.cleaned_data["departamento"],
            shor_name = form.cleaned_data["shorname"],
        )
        
        depa.save()

        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellidos"]

        Personas.objects.create(
            first_name=nombre,
            first_lastname = apellido,
            departamento=depa


        )

        return super(NewRegisterDpto, self).form_validate(form)

class ListDpto(ListView):
    template_name = "departamento/list_dpto.html"
    model = Departamento


    