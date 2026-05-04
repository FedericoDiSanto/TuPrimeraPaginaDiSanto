from django.shortcuts import render, get_object_or_404, redirect
from .models import Jugador, Seleccion, Partido
from django.db.models import Q
from .forms import JugadorForm, SeleccionForm, PartidoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
    
def home(request):
    return render(request, "mundial/home.html")

def listar_jugadores_por_seleccion(request, id):
    seleccion = get_object_or_404(Seleccion, id=id)
    jugadores = Jugador.objects.filter(seleccion=seleccion)
    return render(request, "mundial/listar_jugadores_por_seleccion.html", {"seleccion": seleccion, "jugadores": jugadores})

def detalle_jugador(request, id):
    jugador = get_object_or_404(Jugador,id=id)
    return render(request, "mundial/detalle_jugador.html", {"jugador": jugador})

def listar_selecciones(request):
    selecciones = Seleccion.objects.all()
    return render(request, "mundial/listar_selecciones.html", {"selecciones": selecciones})


class PartidoListView(ListView):
    model = Partido
    template_name = "mundial/listar_partidos.html"
    context_object_name = "partidos"
    

class PartidoDetailView(DetailView):
    model = Partido
    template_name = "mundial/detalle_partido.html"
    context_object_name = "partido"

def buscar_jugador(request):
    nombre = request.GET.get("nombre")
    jugadores = []
    if nombre:
        jugadores = Jugador.objects.filter(
            Q (nombre__icontains = nombre) | Q (apellido__icontains = nombre)
        )
    return render(request, "mundial/buscar_jugador.html", {"jugadores": jugadores, "nombre": nombre})

@login_required
def crear_jugador(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)

        if form.is_valid():
            jugador = form.save(commit=False)
            jugador.representante = request.user
            jugador.save()
            return redirect ("mundial:home")
        
    else:
        form = JugadorForm()
    return render(request, "mundial/crear_jugador.html", {"form": form})

@login_required
def crear_seleccion(request):
    if request.method == "POST":
        form = SeleccionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("mundial:home")
        
    else:
        form = SeleccionForm()
    return render(request, "mundial/crear_seleccion.html", {"form": form})


class PartidoCreateView(LoginRequiredMixin, CreateView):
    model = Partido
    form_class = PartidoForm
    template_name = "mundial/crear_partido.html"

    def get_success_url(self):
        return reverse_lazy(
            "mundial:detalle_partido",
            kwargs={"pk": self.object.pk}
        )
    
    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class PartidoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Partido
    form_class = PartidoForm
    template_name = "mundial/crear_partido.html"

    def get_success_url(self):
        return reverse_lazy(
            "mundial:detalle_partido",
            kwargs={"pk": self.object.pk}
        )
    def test_func(self):
        partido = self.get_object()
        return (
            self.request.user.is_superuser or
            partido.creador == self.request.user
        )
    
class PartidoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Partido
    template_name = "mundial/confirmar_borrado.html"
    success_url = reverse_lazy("mundial:listar_partidos")
    context_object_name = "partido"

    def test_func(self):
        partido = self.get_object()
        return (
            self.request.user.is_superuser  or
            partido.creador == self.request.user
        )

class JugadorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = "mundial/crear_jugador.html"

    def get_success_url(self):
        return reverse_lazy(
            "mundial:detalle_jugador",
            kwargs={"id": self.object.id}
        )
    
    def test_func(self):
        jugador = self.get_object()
        return (
            self.request.user.is_superuser or
            jugador.representante == self.request.user
        )
    
class JugadorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jugador
    template_name = "mundial/confirmar_borrado.html"
    success_url = reverse_lazy("mundial:listar_selecciones")
    context_object_name = "jugador"

    def test_func(self):
        jugador = self.get_object()
        return (
            self.request.user.is_superuser or
            jugador.representante == self.request.user
        )

def about(request):
    return render(request, "mundial/about.html")