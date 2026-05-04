from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    RegisterView,
    ver_perfil,
    crear_perfil,
    editar_perfil,
    CustomPasswordChangeView,
    CustomPasswordChangeDoneView,
)

app_name = "cuentas"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name ="login"),
    path("registro/", RegisterView.as_view(), name ="registro"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("perfil/", ver_perfil, name="perfil"),
    path("crear_perfil/", crear_perfil, name="crear_perfil"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
    path("cambiar_contraseña/", CustomPasswordChangeView.as_view(), name="cambiar_contraseña"),
    path("cambiar_contraseña/hecho/", CustomPasswordChangeDoneView.as_view(), name="cambio_contraseña_hecho"),
]
