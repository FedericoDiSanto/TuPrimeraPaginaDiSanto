from django.contrib import admin
from .models import Jugador, Seleccion, Partido

class JugadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "posicion", "seleccion", "representante")
    list_filter = ("posicion", "seleccion")
    search_fields = ("nombre", "apellido", "seleccion__nombre")
    list_display_links = ("apellido",)
    ordering = ("seleccion",)

class SeleccionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "grupo")
    list_filter = ("grupo",)
    search_fields = ("nombre",)

class PartidoAdmin(admin.ModelAdmin):
    list_display = ("seleccion_local", "seleccion_visitante", "goles_local", "goles_visitante", "fase_torneo")
    list_filter =("fase_torneo", "seleccion_local", "seleccion_visitante")
    search_fields = ("seleccion_local__nombre", "seleccion_visitante__nombre")
    list_display_links = ("fase_torneo",)

admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Seleccion, SeleccionAdmin)
admin.site.register(Partido, PartidoAdmin)