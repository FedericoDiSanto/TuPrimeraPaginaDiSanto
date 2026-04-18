from django.shortcuts import render, get_object_or_404, redirect
from .models import Jugador, Seleccion, Partido
from django.db.models import Q
from .forms import JugadorForm, SeleccionForm, PartidoForm

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

def listar_partidos(request):
    partidos = Partido.objects.all()
    return render(request, "mundial/listar_partidos.html", {"partidos": partidos})

def detalle_partido(request, id):
    partido = get_object_or_404(Partido, id=id)
    return render(request, "mundial/detalle_partido.html", {"partido": partido})

def buscar_jugador(request):
    nombre = request.GET.get("nombre")
    jugadores = []
    if nombre:
        jugadores = Jugador.objects.filter(
            Q (nombre__icontains = nombre) | Q (apellido__icontains = nombre)
        )
    return render(request, "mundial/buscar_jugador.html", {"jugadores": jugadores})

def crear_jugador(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)

        if form.is_valid():
            jugador = form.save(commit=False)
            
            if request.user.is_authenticated:
                jugador.representante = request.user
            jugador.save()
            return redirect ("mundial:home")
        
    else:
        form = JugadorForm()
    return render(request, "mundial/crear_jugador.html", {"form": form})

def crear_seleccion(request):
    if request.method == "POST":
        form = SeleccionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("mundial:home")
        
    else:
        form = SeleccionForm()
    return render(request, "mundial/crear_seleccion.html", {"form": form})

def crear_partido(request):
    if request.method == "POST":
        form = PartidoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("mundial:home")
        
    else:
        form = PartidoForm()
    return render(request, "mundial/crear_partido.html", {"form": form})