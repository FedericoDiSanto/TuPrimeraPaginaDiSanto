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
        fields = ("seleccion_local", "seleccion_visitante", "goles_local", "goles_visitante", "fase_torneo", "estadio", "fecha_partido", "imagen", "codigo")
        widgets = {
            "goles_local": forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
                }),
            "goles_visitante": forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
                }),
            "estadio": forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Estadio Miami'
            }),
            "fecha_partido": forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            "seleccion_local": forms.Select(attrs={
                'class': 'form-control',
            }),
            "seleccion_visitante": forms.Select(attrs={
                'class': 'form-control',
            }),
            "fase_torneo": forms.Select(attrs={
                'class': 'form-control',
            }),
            "imagen": forms.FileInput(attrs={
                'class': 'form-control',
            }),
            "codigo": forms.NumberInput(attrs={
                'class': 'form-control',
                "min": 1,
                "placeholder": "Codigo unico del partido"
            }),
        }