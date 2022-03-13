from rest_framework import viewsets, status, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from mascotas.permissions import IsAdminOrReadOnly
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from directorio.models import User
# Serializers
from mascotas.serializers import AdoptSerializer, ApadrinarSerializer, EventoSerializer, FichaClinicaSerializer, MascotaSerializer, MiembroSerializer, ProvinciaSerializer, ReportSerializer, TiendaSerializer, TrabajadorSerializer, UserLoginSerializer, UserSignupSerializer, VeterinarioSerializer

# Models
from mascotas.models import Adopt, Apadrinar, Evento, FichaClinica, Mascota, Miembro, Provincia, Report, Tienda, Trabajador, Veterinario


# Create your views here.
class AdoptViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = Adopt.objects.all()
    serializer_class = AdoptSerializer
    filter_backends = [DjangoFilterBackend]
    # permission_classes = [IsAuthenticated]

    # filterset_fields = (
    #     'status',
    #     'ci',
    # )

class ReportViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    # permission_classes = [IsAuthenticated]

    filterset_fields = (
        'provincia',
        'tipo_reporte',
        'municipio',
        'status'
    )

class MascotaViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    # permission_classes = [IsAuthenticated]

    filterset_fields = (
        'provincia',
        'status',
        'especie',
        'municipio',
    )

class VeterinarioViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    # permission_classes = [IsAuthenticated]

    filterset_fields = (
        'provincia',
        'municipio',
        'status'
    )

class TrabajadorViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    # permission_classes = [IsAuthenticated]

class MiembroViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    # permission_classes = [IsAuthenticated]

    filterset_fields = (
        'provincia',
    )

class FichaClinicaViewSet(viewsets.ModelViewSet):

    queryset = FichaClinica.objects.all()
    serializer_class = FichaClinicaSerializer
    # permission_classes = [IsAuthenticated]

class ApadrinarViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    queryset = Apadrinar.objects.all()
    serializer_class = ApadrinarSerializer
    # permission_classes = [IsAuthenticated]

    filterset_fields = (
        'provincia',
    )

class TiendaViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
    # permission_classes = [IsAuthenticated]

    filterset_fields = (
        'provincia',
        'municipio'
    )
class EventoViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    # permission_classes = [IsAuthenticated]

class ProvinciaViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    # permission_classes = [IsAuthenticated]

    filterset_fields = (
        'provincia',
    )

class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSignupSerializer


    @action(detail=False, methods=['post'])
    def login(self, request):
        """User login"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(status=status.HTTP_201_CREATED)

