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
from mascotas.models import Miembro, Trabajador

from mascotas.views import ApadrinarViewSet, EventoViewSet, FichaClinicaViewSet
from mascotas.views import MascotaViewSet, MiembroViewSet, ProvinciaViewSet, ReportViewSet
from mascotas.views import AdoptViewSet, TiendaViewSet, TrabajadorViewSet, VeterinarioViewSet

router = DefaultRouter()

router.register(r'reportes', ReportViewSet, basename='report')
router.register(r'adopciones', AdoptViewSet, basename='adopt')
router.register(r'mascotas', MascotaViewSet, basename='mascota')

router.register(r'clinicas', VeterinarioViewSet, basename='veterinario')
router.register(r'trabajos', TrabajadorViewSet, basename='trabajador')
router.register(r'miembros', MiembroViewSet, basename='miembro')
router.register(r'fichasclinicas', FichaClinicaViewSet, basename='fichaclinica')
router.register(r'apadrinar', ApadrinarViewSet, basename='apadrinar')
router.register(r'tiendas', TiendaViewSet, basename='tienda')
router.register(r'eventos', EventoViewSet, basename='evento')
router.register(r'provincias', ProvinciaViewSet, basename='provincia')



urlpatterns = [
    path('', include(router.urls)),
]