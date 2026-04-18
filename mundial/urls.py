from django.urls import path
from .views import home, listar_jugadores_por_seleccion, detalle_jugador, listar_selecciones, listar_partidos, detalle_partido, buscar_jugador, crear_jugador, crear_seleccion, crear_partido

app_name = "mundial"

urlpatterns = [
    path("", home, name="home"),
    path("listar_jugadores_por_seleccion/<int:id>/", listar_jugadores_por_seleccion, name="listar_jugadores_por_seleccion"),
    path("detalle_jugador/<int:id>/", detalle_jugador, name="detalle_jugador"),
    path("listar_selecciones/", listar_selecciones, name="listar_selecciones"),
    path("listar_partidos/", listar_partidos, name="listar_partidos"),
    path("detalle_partido/<int:id>/", detalle_partido, name="detalle_partido"),
    path("buscar_jugador/", buscar_jugador, name="buscar_jugador"),
    path("crear_jugador/", crear_jugador, name="crear_jugador"),
    path("crear_seleccion/", crear_seleccion, name="crear_seleccion"),
    path("crear_partido/", crear_partido, name="crear_partido"),
]