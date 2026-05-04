from django.db import models
from django.contrib.auth.models import User

class Jugador(models.Model):

    class Posicion(models.TextChoices):
        ARQUERO = "AR", "Arquero"
        DEFENSOR = "DF", "Defensor"
        MEDIOCAMPISTA = "MC", "Mediocampista"
        DELANTERO = "DL", "Delantero"
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    posicion = models.CharField(max_length=2, choices=Posicion.choices)
    seleccion = models.ForeignKey("Seleccion", on_delete=models.CASCADE)
    edad = models.IntegerField(default=18)
    goles = models.IntegerField(default=0)
    representante = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__ (self):
        return f"{self.nombre} {self.apellido} - {self.seleccion.nombre}"


class Seleccion(models.Model):
    
    class Grupo(models.TextChoices):
        A = "A", "Grupo A"
        B = "B", "Grupo B"
        C = "C", "Grupo C"
        D = "D", "Grupo D"
        E = "E", "Grupo E"
        F = "F", "Grupo F"
        G = "G", "Grupo G"
        H = "H", "Grupo H"

    nombre = models.CharField(max_length=50)
    grupo = models.CharField(max_length=1, choices= Grupo.choices)

    def __str__(self):
        return f"{self.nombre}"
    

class Partido(models.Model):

    class Fase_torneo(models.TextChoices):
        FASE_DE_GRUPO = "FG", "Fase de Grupo"
        DIECISEISAVOS = "16", "Dieciseisavos"
        OCTAVOS = "8", "Octavos"
        CUARTOS = "4", "Cuartos"
        SEMIFINAL = "SF", "Semifinal"
        FINAL = "F", "Final"

    seleccion_local = models.ForeignKey("Seleccion", on_delete=models.CASCADE, related_name="partidos_local")
    seleccion_visitante = models.ForeignKey("Seleccion", on_delete=models.CASCADE, related_name="partidos_visitante")
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    fase_torneo = models.CharField(max_length=2, choices= Fase_torneo.choices)
    estadio = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='estadios', null=True, blank=True)
    fecha_partido = models.DateField()
    codigo = models.IntegerField(unique=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.seleccion_local} vs {self.seleccion_visitante} ({self.fase_torneo})"