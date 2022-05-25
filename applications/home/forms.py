from django import forms

from .models import Prueba_Dpto

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba_Dpto
        fields = ["titulo","subtitulo","cantidad"]

        widgets = {
            "titulo" : forms.TextInput(attrs={"placeholder": "Ingrese Texto Aqui"}),
            "cantidad" : forms.TextInput(attrs={"placeholder":"Ingrese Numero Aqui"})
        }
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError("Ingrese un numero mayor a 10")
        
        return cantidad
