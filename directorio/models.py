from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from mascotas.models import Municipio, Provincia

# Create your models here.


class User(AbstractUser):

    adress          = models.CharField(max_length=255, blank=True, default="")
    phone           = models.CharField(max_length=15, blank=True, default="")
    imagen          = models.ImageField(upload_to='users/', blank=True, null=True)
    provincia       = models.CharField(max_length=100, blank=True, default="")
    municipio       = models.CharField(max_length=100, blank=True, default="")
    ci              = models.CharField(max_length=11, blank=True, default="")
    descripcion     = models.CharField(max_length=50, blank=True, default="")
    email           = models.EmailField(_('email address'), unique=True, default="")
    # REQUIRED_FIELDS = [
    #     'adress',
    #     'phone',
    #     'email',
    #     'first_name',
    #     'last_name',
    #     'imagen',
    #     'provincia',
    #     'municipio',
    #     'ci',
    #     'descripcion'
    # ]
