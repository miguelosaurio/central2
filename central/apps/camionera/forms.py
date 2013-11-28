from django.forms import ModelForm
from django import forms
from central.apps.camionera.models import *

class reservacionForm(ModelForm):
	class Meta:
		model = reservacion
		exclude =('fechaAproxSalida','status','fechaAbordar','viaje','asiento')

		
class paradaForm(ModelForm):
	class Meta:
		model = viaje_parada
		
class abordarForm(ModelForm):
	class Meta:
		model = abordar

'''
viaje = viaje.objects.filter(id=)
class reservacionesForm(forms.Form):
	viaje = forms.ModelChoiceField(queryset=viaje.objects.filter(status=True))
	origen =  forms.ModelChoiceField(queryset=ruta_parada.objects.all())
	destino = forms.ModelChoiceField(queryset=)
	asiento froms.ModelChoiceField(queryset=asiento.objects.all())
	nombre = forms.CharField(widget=forms.TextInput())
	apellidos = forms.CharField(widget=forms.TextInput())
'''