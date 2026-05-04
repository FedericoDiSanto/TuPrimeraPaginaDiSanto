from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
        }

class PerfilForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={"class":"form-control", "type":"date"}),
        input_formats=["%Y-%m-%d"],
    )
    class Meta:
        model = Perfil
        fields = ("fecha_nacimiento", "dni", "biografia", "avatar")
        widgets = {
            "biografia": forms.Textarea(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class":"form-control"}),
        }
