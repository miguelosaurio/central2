# Create your views here.
from django.http import HttpResponse
from central.apps.camionera.models import *
from django.core import serializers

def wsViajes_view(request):
	data = serializers.serialize("json",viaje.objects.filter(status=True))
	return HttpResponse(data,mimetype="application/json")