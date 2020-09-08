from django.conf.urls import url, include
from apps.usuario.views import RegistroUsuario

urlpatterns = [
   
    url(r'^nuevo$', RegistroUsuario.as_view(), name='Registrar'),
]