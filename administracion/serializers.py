from rest_framework import serializers
from directorio.models import User
from mascotas.models import Apadrinar, Evento, FichaClinica, Mascota, Municipio, Provincia, Veterinario
from mascotas.models import Miembro, Report, Adopt, Tienda, Trabajador


# Create your models here.

class ReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report

        fields = "__all__"

class MascotaSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Mascota

        fields = "__all__"

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

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = "__all__"