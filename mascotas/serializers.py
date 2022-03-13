from directorio.models import User
from django.db.models.query import QuerySet
from rest_framework import serializers
from mascotas.models import Apadrinar, Evento, FichaClinica, Mascota, Municipio, Provincia, Veterinario
from mascotas.models import Miembro, Report, Adopt, Tienda, Trabajador
from django.contrib.auth import authenticate, login, logout, password_validation
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


class ReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report

        fields = "__all__"

class MascotaSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Mascota

        fields = "__all__"

        read_only_fields = ('status',)

class AdoptSerializer(serializers.ModelSerializer):
    
    # mascota = serializers.StringRelatedField()

    class Meta:
        model = Adopt

        fields = "__all__"

class VeterinarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veterinario

        fields = "__all__"

class FichaClinicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = FichaClinica

        fields = "__all__"
        
class MiembroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Miembro

        fields = "__all__"
        
class TrabajadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trabajador

        fields = "__all__"       
        
class MunicipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio

        fields = "__all__"

class ProvinciaSerializer(serializers.ModelSerializer):
    
    municipio = MunicipioSerializer(many=True)

    class Meta:
        model = Provincia

        fields = "__all__"

class ApadrinarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apadrinar

        fields = "__all__"  

class TiendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tienda

        fields = "__all__" 

class EventoSerializer(serializers.ModelSerializer):

    def validate(self, data):
        
        if 'imagen' not in data and 'descripcion' not in data:
            raise serializers.ValidationError("Debe poner una descripcion o una imagen al menos")
        
        return super().validate(data)

    class Meta:
        model = Evento

        fields = "__all__" 

class UserSignupSerializer(serializers.Serializer):
    
    password = serializers.CharField(min_length=8, max_length=64)
    passwd_conf = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['passwd_conf']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        data.pop('passwd_conf')
        user = User.objects.create_user(**data)
        return user

class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardar el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key