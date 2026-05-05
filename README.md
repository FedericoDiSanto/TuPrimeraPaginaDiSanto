Proyecto Mundial 2026


Descripción
Aplicación web desarrollada en Django que simula un Mundial de Fútbol.
Permite gestionar jugadores, selecciones y partidos, con sistema de autenticación de usuarios y perfiles personalizados.


Funcionalidades
* CRUD completo de partidos
* CRUD completo de jugadores
* Listar selecciones
* Crear selecciones 
* Buscar jugadores por nombre o apellido


Usuarios (app cuentas)
- Registro de usuarios
- Login y logout
- Perfil de usuario (crear, ver y editar)
- Cambio de contraseña

Seguridad
- Login obligatorio para la mayoría de las acciones
- Permisos en actualizacion y eliminación de partidos:
     Solo el creador o superusuario puede borrar
- Permisos en actualizacion y eliminación de jugadores:
     Solo el creador o superusuario puede borrar
- Uso de LoginRequiredMixin y decoradores @login_required


Modelos

Jugador
- nombre
- apellido
- posición
- edad
- goles
- selección (FK)
- representante (User)

Selección
- nombre
- grupo (A–H)

Partido
- selección local (FK)
- selección visitante (FK)
- goles local / visitante
- fase del torneo
- estadio
- fecha
- imagen
- código único
- creador (User)

Perfil
- usuario (OneToOne con User)
- avatar (con imagen por defecto)
- biografía
- fecha de nacimiento
- DNI


Orden recomendado para probar
1. Ir a "Crear selección" y crear al menos una selección
2. Ir a "Crear jugador" y asignarlo a una selección
3. Ir a "Crear partido", seleccionar equipos y cargar el resultado
4. Probar "Lista de selecciones" y entrar a cada una
5. Probar "Lista de partidos"
6. Probar "Buscar jugador"


Autenticación
Configuración utilizada:
- LOGIN_URL = cuentas:login
- LOGIN_REDIRECT_URL = mundial:home
- LOGOUT_REDIRECT_URL = cuentas:login


Notas
- El representante del jugador se asigna automáticamente si el usuario está logueado
- Si no hay usuario logueado, el jugador se crea sin representante
- El perfil de usuario no se crea automáticamente, se genera manualmente desde una vista de creación de perfil.
- El avatar del perfil tiene imagen por defecto si el usuario no sube una.


Estado del proyecto
* CRUD completo funcional  
* Autenticación completa  
* Sistema de perfiles implementado  
* Permisos por usuario  
* Media configurado  
* Templates organizados  


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
+ mundial/ → app principal del proyecto (jugadores, selecciones, partidos)
+ cuentas/ → autenticación y perfiles
+ templates/ → vistas HTML organizadas por app
+ media/ → imágenes de usuarios (avatars)


Video del proyecto
En el siguiente enlace se puede ver una demostración completa del funcionamiento de la aplicación:   
https://drive.google.com/file/d/1ABuYGZ68dLqxd_iSKKvj1xtOb8Y9WhUn/view?usp=sharing