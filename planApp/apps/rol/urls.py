from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.rol.views import rol_list, rol_create, rol_edit, rol_delete

urlpatterns = [
    url(r'^$', rol_list, name='index'),
    url(r'^nuevo$', rol_create, name='rol_crear'),
    url(r'^editar/(?P<id>\d+)/$', rol_edit, name='rol_editar'),
    url(r'^eliminar/(?P<id>\d+)/$', rol_delete, name='rol_eliminar'),
]
