from django_filters.rest_framework import DjangoFilterBackend
# Django REST Framework
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
# Serializers
from administracion.serializers import (
                                UserModelSerializer,
                                AdoptSerializer,
                                ApadrinarSerializer,
                                EventoSerializer,
                                FichaClinicaSerializer,
                                MascotaSerializer,
                                MiembroSerializer,
                                ProvinciaSerializer,
                                ReportSerializer,
                                TiendaSerializer,
                                TrabajadorSerializer,
                                VeterinarioSerializer
                                )

# Models
from mascotas.models import (
                            Adopt,
                            Apadrinar,
                            Evento,
                            FichaClinica,
                            Mascota,
                            Miembro,
                            Provincia,
                            Report,
                            Tienda,
                            Trabajador,
                            Veterinario
                            )
from directorio.models import User

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAdminUser]

class AdoptViewSet(viewsets.ModelViewSet):

    queryset = Adopt.objects.all()
    serializer_class = AdoptSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAdminUser]

    # filterset_fields = (
    #     'status',
    #     'ci',
    # )

class ReportViewSet(viewsets.ModelViewSet):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]

    filterset_fields = (
        'provincia',
        'tipo_reporte',
        'municipio',
        'status'
    )

class MascotaViewSet(viewsets.ModelViewSet):

    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [IsAdminUser]

    filterset_fields = (
        'provincia',
        'status',
        'especie',
        'municipio',
    )

class VeterinarioViewSet(viewsets.ModelViewSet):

    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    permission_classes = [IsAdminUser]

    filterset_fields = (
        'provincia',
        'municipio',
        'status'
    )

class TrabajadorViewSet(viewsets.ModelViewSet):

    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAdminUser]

class MiembroViewSet(viewsets.ModelViewSet):

    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    permission_classes = [IsAdminUser]

    filterset_fields = (
        'provincia',
    )

class FichaClinicaViewSet(viewsets.ModelViewSet):

    queryset = FichaClinica.objects.all()
    serializer_class = FichaClinicaSerializer
    permission_classes = [IsAdminUser]

class ApadrinarViewSet(viewsets.ModelViewSet):

    queryset = Apadrinar.objects.all()
    serializer_class = ApadrinarSerializer
    permission_classes = [IsAdminUser]

    filterset_fields = (
        'provincia',
    )

class TiendaViewSet(viewsets.ModelViewSet):

    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
    permission_classes = [IsAdminUser]

    filterset_fields = (
        'provincia',
        'municipio'
    )
class EventoViewSet(viewsets.ModelViewSet):

    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAdminUser]

class ProvinciaViewSet(viewsets.ModelViewSet):

    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = [IsAdminUser]

    filterset_fields = (
        'provincia',
    )