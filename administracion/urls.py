"""Mascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter
from django.urls import path, include

from administracion.views import ApadrinarViewSet, EventoViewSet, FichaClinicaViewSet
from administracion.views import MascotaViewSet, MiembroViewSet, ProvinciaViewSet, ReportViewSet
from administracion.views import AdoptViewSet, TiendaViewSet, TrabajadorViewSet, VeterinarioViewSet
from administracion.views import UserViewSet

router = DefaultRouter()

router.register(r'reportes', ReportViewSet, basename='admin-report')
router.register(r'adopciones', AdoptViewSet, basename='admin-adopt')
router.register(r'mascotas', MascotaViewSet, basename='admin-mascota')

router.register(r'clinicas', VeterinarioViewSet, basename='admin-veterinario')
router.register(r'trabajos', TrabajadorViewSet, basename='admin-trabajador')
router.register(r'miembros', MiembroViewSet, basename='admin-miembro')
router.register(r'fichasclinicas', FichaClinicaViewSet, basename='admin-fichaclinica')
router.register(r'apadrinar', ApadrinarViewSet, basename='admin-apadrinar')
router.register(r'tiendas', TiendaViewSet, basename='admin-tienda')
router.register(r'eventos', EventoViewSet, basename='admin-evento')
router.register(r'provincias', ProvinciaViewSet, basename='admin-provincia')
router.register(r'usuarios', UserViewSet, basename='admin-usuario')



urlpatterns = [
    path('', include(router.urls)),
]