# from django.contrib import admin
from django_restful_admin import admin as rest_admin
from mascotas.models import Report, Adopt, Mascota, Veterinario, Trabajador
from mascotas.models import Apadrinar, Miembro, FichaClinica, Tienda, Evento
from mascotas.models import Provincia, Municipio
from directorio.models import User
from django.contrib.auth.models import Group, Permission
# from django.contrib import admin

# Register your models here.

rest_admin.site.register(Group)
rest_admin.site.register(Permission)
rest_admin.site.register(Report)
rest_admin.site.register(Adopt)
rest_admin.site.register(Mascota)
rest_admin.site.register(Veterinario)
rest_admin.site.register(Trabajador)
rest_admin.site.register(Apadrinar)
rest_admin.site.register(Miembro)
rest_admin.site.register(FichaClinica)
rest_admin.site.register(Tienda)
rest_admin.site.register(Evento)
rest_admin.site.register(Provincia)
rest_admin.site.register(Municipio)

# admin.site.register(Report)
# admin.site.register(Adopt)
# admin.site.register(Mascota)
# admin.site.register(Veterinario)
# admin.site.register(Trabajador)
# admin.site.register(Apadrinar)
# admin.site.register(Miembro)
# admin.site.register(FichaClinica)
# admin.site.register(Tienda)
# admin.site.register(Evento)
# admin.site.register(Provincia)
# admin.site.register(Municipio)