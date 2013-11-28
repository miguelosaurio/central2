from django.conf.urls import patterns, include, url
from central.apps.camionera.views import *

urlpatterns = patterns('central.apps.camionera.views',
	#views
    url(r'^ciudades/', 'ciudadesView'),
	url(r'^viajesDisponibles/','viajesView'),
	#formularios
	url(r'^parada/','formParada'),
	url(r'^abordar/','formAbordar'),
	url(r'^reservarViaje/(?P<id>.*)/$','formReservacion'),

)
