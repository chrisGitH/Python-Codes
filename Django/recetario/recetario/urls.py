from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),

    #Url de la aplicacion
    url(r'^$','principal.views.index'),
    url(r'^usuarios/', 'principal.views.usuarios'),
    url(r'^receta/(?P<id>\d+)$', 'principal.views.detalle_receta'),
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^ajax/','principal.views.ajax'),
    url(r'^nueva-receta/$', 'principal.views.nueva_receta'),
    url(r'^comentario/$', 'principal.views.comentario')
)
