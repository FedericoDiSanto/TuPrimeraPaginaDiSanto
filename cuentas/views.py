from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm
from django.shortcuts import get_object_or_404
from .models import Perfil
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/registro.html"
    success_url = reverse_lazy("cuentas:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data["email"]
        user.save()
        return super().form_valid(form)
    
@login_required
def crear_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            request.user.first_name = request.POST.get("first_name", "")
            request.user.last_name = request.POST.get("last_name", "")
            request.user.save()
            return redirect("cuentas:perfil")
    else:
        form = PerfilForm()

    return render(request, "cuentas/crear_perfil.html", {"form":form})

@login_required
def ver_perfil(request):
    if not hasattr(request.user, "perfil"):
        return redirect("cuentas:crear_perfil")
    
    perfil = request.user.perfil
    return render(request, "cuentas/perfil.html", {"perfil":perfil})

@login_required
def editar_perfil(request):
    if not hasattr(request.user, "perfil"):
        return redirect("cuentas:crear_perfil")
    perfil = request.user.perfil
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            request.user.first_name = request.POST.get("first_name")
            request.user.last_name = request.POST.get("last_name")
            request.user.save()
            return redirect("cuentas:perfil")
    else:
        form = PerfilForm(instance=perfil, initial={
            "nombre": request.user.first_name,
            "apellido": request.user.last_name,
        })

    return render(request, "cuentas/editar_perfil.html", {"form":form})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "registration/cambiar_contraseña.html"
    success_url = reverse_lazy("cuentas:cambio_contraseña_hecho")

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/cambio_contraseña_hecho.html"