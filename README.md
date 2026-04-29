Proyecto Mundial 2026

Funcionalidades
* Listar selecciones
* Ver jugadores por selección
* Ver detalle de jugador
* Listar partidos
* Ver detalle de partido
* Crear jugadores, selecciones y partidos
* Buscar jugadores por nombre o apellido


Orden recomendado para probar
1. Ir a "Crear selección" y crear al menos una selección
2. Ir a "Crear jugador" y asignarlo a una selección
3. Ir a "Crear partido", seleccionar equipos y cargar el resultado
4. Probar "Lista de selecciones" y entrar a cada una
5. Probar "Lista de partidos"
6. Probar "Buscar jugador"


Notas
- El representante del jugador se asigna automáticamente si el usuario está logueado
- Si no hay usuario logueado, el jugador se crea sin representante


Levantar el proyecto (Mac)
1. Clonar el repositorio
    git clone https://github.com/FedericoDiSanto/TuPrimeraPaginaDiSanto.git
    cd TuPrimeraPaginaDiSanto

2. Crear entorno virtual
    python3 -m venv venv

3. Activar entorno virtual
    Mac / Linux:
        source venv/bin/activate
    Windows:
        venv\Scripts\activate

4. Instalar dependencias
    pip install -r requirements.txt

5. Aplicar migraciones
    python3 manage.py migrate

6. Crear superusuario (opcional)
    python3 manage.py createsuperuser

7. Correr el servidor
    python3 manage.py runserver


Acceso al proyecto:
http://127.0.0.1:8000/


Estructura del proyecto
+ proyecto_mundial/ → configuración principal Django
+ mundial/ → app principal del proyecto