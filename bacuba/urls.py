"""bacuba URL Configuration

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
# from django.contrib import admin
from django_restful_admin import admin as rest_admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static







urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('mascotas.urls')),
    path('api-admin/', rest_admin.site.urls),
    path('api-admin2/', include('administracion.urls')),
    path('', include('directorio.urls')),
    path(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)