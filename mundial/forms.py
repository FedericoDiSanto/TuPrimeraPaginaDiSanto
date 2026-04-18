from django import forms
from .models import Jugador, Seleccion, Partido

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ("nombre", "apellido", "posicion", "seleccion", "edad")
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "edad": forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SeleccionForm(forms.ModelForm):
    class Meta:
        model = Seleccion
        fields = ("nombre", "grupo")
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
        }

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ("seleccion_local", "seleccion_visitante", "goles_local", "goles_visitante", "fase_torneo")
        widgets = {
            "goles_local": forms.NumberInput(attrs={'class': 'form-control'}),
            "goles_visitante": forms.NumberInput(attrs={'class': 'form-control'}),
        }
