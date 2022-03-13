from email.policy import default
from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Provincia(models.Model):

    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("provincia-detail", kwargs={"pk": self.pk})
    
class Municipio(models.Model):
    
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre    = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("municipio-detail", kwargs={"pk": self.pk})

ESPECIES_CHOICES = [
    ['Gato','Gato'],
    ['Perro','Perro'],
    ['Otra','Otra'],
]

class Mascota(models.Model):

    imagen           = models.ImageField(upload_to='mascotas/')
    nombre           = models.CharField(max_length=50)
    direccion        = models.CharField(max_length=255)
    sexo             = models.CharField(max_length=50)
    edad             = models.CharField(max_length=50)
    provincia        = models.CharField(max_length=50)
    municipio        = models.CharField(max_length=50)
    descripcion      = models.CharField(max_length=250, default='')
    peso             = models.FloatField()
    especie          = models.CharField(max_length=50, choices=ESPECIES_CHOICES)
    fecha            = models.DateField(auto_now=True)
    status           = models.IntegerField(default=0)
    comunicacion     = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("mascota-detail", kwargs={"pk": self.pk})

class FichaClinica(models.Model):

    mascota         = models.ForeignKey(Mascota, verbose_name="mascota_id", on_delete=models.DO_NOTHING)
    identificacion  = models.BooleanField()
    vacuna          = models.BooleanField()
    desparacitacion = models.BooleanField() 
    esterilizacion  = models.BooleanField()
    leishmania      = models.BooleanField()
    filaria         = models.BooleanField()
    ppp             = models.BooleanField()
    fecha_creacion  = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "fichaclinica"
        verbose_name_plural = "fichasclinicas"

    def __str__(self):
        return self.mascota.nombre

    def get_absolute_url(self):
        return reverse("fichaclinica_detail", kwargs={"pk": self.pk})

class Miembro(models.Model):
    #TODO Agregar patron de telefono
    # usuario   = models.OneToOneField(User, verbose_name="usuario", on_delete=models.CASCADE)
    nombre           = models.CharField(max_length=128)
    ci        = models.CharField(max_length=11)
    imagen = models.ImageField(upload_to='miembros/perfil/')
    imagen_ci    = models.ImageField(upload_to='miembros/ci/')
    dirección = models.CharField(max_length=255)
    provincia = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    tipo      = models.CharField(max_length=50)
    telefono  = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    fecha     = models.DateField(_("fecha"), auto_now=True)
    status    = IntegerField()
    
    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("miembro-detail", kwargs={"pk": self.pk})
    
class Trabajador(models.Model):
    #TODO Agregar patron de telefono
    # usuario        = models.OneToOneField(User, verbose_name="usuario", on_delete=models.CASCADE)
    nombre         = models.CharField(max_length=50)
    email          = models.EmailField(max_length=254)
    telefono       = models.CharField(max_length=50)
    web            = models.URLField(max_length=200)
    descripción    = models.CharField(max_length=500)
    consentimiento = models.BooleanField(default=False)
    tipo           = models.CharField(_("tipo"), max_length=50)
    fecha          = models.DateField(_("fecha"), auto_now=True)
    status         = IntegerField()
    
    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("trabajador-detail", kwargs={"pk": self.pk})

class Veterinario(models.Model):
    #TODO Agregar patron de telefono
    usuario     = models.CharField(max_length=255)
    imgperfil   = models.ImageField(upload_to='veterinarios/')
    dirección   = models.CharField(max_length=255)
    provincia = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    descripción = models.CharField(max_length=255)
    telefono    = models.CharField(max_length=50)
    domicilio   = models.BooleanField()
    fecha       = models.DateField(_("fecha"), auto_now=True)
    status      = IntegerField()
    # recommended = models.BooleanField()
    
    class Meta:
        verbose_name = "Veterinario"
        verbose_name_plural = "Veterinarios"

    def __str__(self):
        return self.usuario

    def get_absolute_url(self):
        return reverse("veterinario-detail", kwargs={"pk": self.pk})


class Adopt(models.Model):

    mascota          = models.ForeignKey(Mascota, verbose_name='mascota', on_delete=models.CASCADE)
    nombre           = models.CharField(max_length=50)
    direccion        = models.CharField("direction", max_length=255)
    provincia        = models.CharField(max_length=50)
    municipio        = models.CharField(max_length=50)
    ci               = models.CharField("ci", max_length=11)
    email            = models.EmailField("email", max_length=254, validators=[EmailValidator])
    q1               = models.CharField(max_length=128)
    q2               = models.BooleanField()
    q3               = models.BooleanField()
    q4               = models.BooleanField()
    q5               = models.BooleanField()
    q6               = models.BooleanField()
    q7               = models.CharField(max_length=128)
    q8               = models.BooleanField()
    q9               = models.BooleanField()
    q10              = models.CharField(max_length=128)
    q11              = models.CharField(max_length=128)
    q12              = models.CharField(max_length=128)
    q13              = models.BooleanField()
    q14              = models.BooleanField()
    q15              = models.BooleanField()
    q16              = models.BooleanField()
    q17              = models.BooleanField()
    status           = models.IntegerField(default=0, blank=True)
    fecha_pedido     = models.DateField(auto_now=True)
    phone = models.CharField("phone", max_length=15) #TODO: APLICARLE VALIDADOR DE EXPRESION REGULAR

    def get_absolute_url(self):
        return reverse("adopt-detail", kwargs={"pk": self.pk})




class Report(models.Model):
    """Model definition for Report."""

    # TODO: Define fields here
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre              = models.CharField("nameReport", max_length=75)
    imagen              = models.ImageField("urlImgPet", upload_to='reports/')
    email               = models.EmailField("email", max_length=254, validators=[EmailValidator])
    telefono            = models.CharField("phone", max_length=15) #TODO: APLICARLE VALIDADOR DE EXPRESION REGULAR
    provincia           = models.CharField(max_length=50)
    municipio           = models.CharField(max_length=50)
    direccion_mascota   = models.CharField(max_length=255)
    tipo_reporte        = models.CharField(max_length=50)
    estadia             = models.BooleanField(_("estadia"), blank=True, default=False)
    desparasitado       = models.BooleanField(blank=True, default=False)
    deshidratado        = models.BooleanField()
    caquexico           = models.BooleanField()
    desnutrido          = models.BooleanField()
    parasitos           = models.BooleanField()
    agresivo            = models.BooleanField()
    depresivo           = models.BooleanField()
    medicamentos        = models.BooleanField()
    veterinario         = models.BooleanField()
    monetario           = models.BooleanField()
    hTemporal           = models.BooleanField()
    tvt                 = models.BooleanField()
    descripcion         = models.CharField(max_length=500)
    fecha               = models.DateField(auto_now=True)
    status              = IntegerField()

    class Meta:
        """Meta definition for Report."""

        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        """Unicode representation of Report."""
        return self.nombre

    def get_absolute_url(self):
        return reverse("report-detail", kwargs={"pk": self.pk})
    
class Tienda(models.Model):
    """Model definition for Tienda."""

    # TODO: Define fields here
    imagen      = models.ImageField(_("imagen"), upload_to='tiendas/')
    nombre      = models.CharField(max_length=50)
    telefono    = models.CharField(max_length=15)
    email       = models.EmailField(max_length=254, blank=True, default="")
    direccion   = models.CharField(max_length=255)
    provincia   = models.CharField(max_length=50)
    municipio   = models.CharField(max_length=50)
    online      = models.BooleanField()
    descripcion = models.CharField(max_length=500)
    domicilio   = models.BooleanField()
    fecha       = models.DateField(auto_now=True)
    status      = IntegerField()
    # recommended = models.BooleanField()

    class Meta:
        """Meta definition for Tienda."""

        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'

    def __str__(self):
        """Unicode representation of Tienda."""
        return self.nombre

    def get_absolute_url(self):
        return reverse("tienda-detail", kwargs={"pk": self.pk})

class Apadrinar(models.Model):

    mascota          = models.ForeignKey(Mascota, verbose_name='mascota', on_delete=models.PROTECT)
    tipo             = models.CharField(max_length=50)
    tiempo           = models.CharField(max_length=50)
    nombre           = models.CharField(max_length=50)
    telefono         = models.CharField( max_length=15) #TODO: APLICARLE VALIDADOR DE EXPRESION REGULAR
    direccion        = models.CharField(max_length=255)
    email            = models.EmailField(max_length=254, validators=[EmailValidator])
    # ci               = models.CharField("ci", max_length=11)
    provincia        = models.CharField(max_length=50)
    municipio        = models.CharField(max_length=50)
    fecha            = models.DateField(auto_now=True)
    status           = IntegerField()
    
    class Meta:
        """Meta definition for Apadrinar."""

        verbose_name = 'Apadrinar'
        verbose_name_plural = 'Apadrinaciones'

    def get_absolute_url(self):
        return reverse("apadrinar-detail", kwargs={"pk": self.pk})

class Evento(models.Model):

    imagen = models.ImageField(upload_to='eventos/', blank=True)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        """Meta definition for Evento."""

        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def get_absolute_url(self):
        return reverse("evento-detail", kwargs={"pk": self.pk})