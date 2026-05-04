from django.urls import path
from .views import(
    home,
    listar_jugadores_por_seleccion,
    detalle_jugador,
    listar_selecciones,
    PartidoListView,
    PartidoDetailView,
    PartidoCreateView,
    PartidoUpdateView,
    PartidoDeleteView,
    buscar_jugador,
    crear_jugador,
    crear_seleccion,
    JugadorUpdateView,
    JugadorDeleteView,
    about,
)

app_name = "mundial"

urlpatterns = [
    path("", home, name="home"),
    path("listar_jugadores_por_seleccion/<int:id>/", listar_jugadores_por_seleccion, name="listar_jugadores_por_seleccion"),
    path("detalle_jugador/<int:id>/", detalle_jugador, name="detalle_jugador"),
    path("listar_selecciones/", listar_selecciones, name="listar_selecciones"),
    path("listar_partidos/", PartidoListView.as_view(), name="listar_partidos"),
    path("detalle_partido/<int:pk>/", PartidoDetailView.as_view(), name="detalle_partido"),
    path("buscar_jugador/", buscar_jugador, name="buscar_jugador"),
    path("crear_jugador/", crear_jugador, name="crear_jugador"),
    path("crear_seleccion/", crear_seleccion, name="crear_seleccion"),
    path("crear_partido/", PartidoCreateView.as_view(), name="crear_partido"),
    path("editar_partido/<int:pk>/", PartidoUpdateView.as_view(), name="editar_partido"),
    path("borrar_partido/<int:pk>/", PartidoDeleteView.as_view(), name="borrar_partido"),
    path("editar_jugador/<int:pk>/", JugadorUpdateView.as_view(), name="editar_jugador"),
    path("borrar_jugador/<int:pk>/", JugadorDeleteView.as_view(), name="borrar_jugador"),
    path("about/", about, name="about"),
]