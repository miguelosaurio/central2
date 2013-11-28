# Create your views here.
from django.shortcuts import render_to_response
from central.apps.camionera.models import *
from django.template import *
from central.apps.camionera.forms import *

def ciudadesView(request):
	ciudades  = ciudad.objects.all()
	return render_to_response('camionera/ciudad.html',{'ciudades':ciudades},context_instance=RequestContext(request))

def viajesView(request):
	viajes = viaje.objects.filter(status=True)
	paradas = ruta_parada.objects.all()
	ctx = {'viajes':viajes,'paradas':paradas}
	return render_to_response('camionera/viajesTrue.html',ctx, context_instance=RequestContext(request))

def formReservacion(request, id):
	via = viaje.objects.get(id=id)
	if request.method == 'POST':
		formulario = reservacionForm(request.POST)
		if formulario.is_valid():
			formulario.save(commit=False)
			#obtener ultima reservacion registrada
			
			ultimo = reservacion.objects.all().count()

			#obtener el id del viaje de la ultima reservacion
				
			viajez = reservacion.objects.filter(id=ultimo).values('viaje')
			v = viajez[0] ['viaje']
			
			#obtener la parada en la que se abordara dicha reservacion

			parad = reservacion.objects.filter(id=ultimo).values('origen')
			par = parad[0] ['origen']
			par = par + 1

			#obtener la ruta a la que pertenece dicha parada
			
			ruta = viaje.objects.filter(id=v).values('ruta')
			r = ruta[0] ['ruta']

			#obtener el tiempo aproximado de traslado de salida de camion a ubicacion actual
			
			taprox = ruta_parada.objects.filter(ruta=r).filter(parada=par).values('tiempoAprox')
			tap = taprox[0] ['tiempoAprox']
			
			#suma de tiempo de salida y tiempo aproximado
			#NO TERMINADO
			
			
			#comparacion de fecha reservacion con resultado de suma anterior
			#NO TERMINADO
			
			
			#contador
			
			conta = viaje.objects.filter(id=v).values('contados')
			cont = cont [0] ['contados']
			
			cami = viaje.objects.filter(id=v).values('camion')
			cam = cami [0] ['camion']
			
			capa = camion.objects.filter(id=cam).values('capacidad')
			cap = capa [0] ['capacidad']
			
			if cont >= cap:
				return HttpResponseRedirect('/URLERROR_AUTOBUSLLENO')
			else:
				#commits 
				#NO TERMINADO
				conta = viaje.objects.filter(id=v).update(contados = cont + 1)
				conta.save()
			
			return HttpResponseRedirect('/Freservacion')
	else:
		formulario = reservacionForm()
	return render_to_response('camionera/Freservacion.html',{'formulario':formulario,'viaje':via}, context_instance = RequestContext(request))

	
def formParada(request):
	if request.method == 'POST':
		formulario = paradaForm(request.POST)
		if formulario.is_valid():
			formulario.save(commit=False)

			#obtener ultima parada registrada
			
			ultimo = viaje_parada.objects.all().count()
			
			#obtener el viaje al que pertenece
			
			viajp = viaje_parada.objects.filter(id = ultimo).values('viaje')
			vp = viajp [0] ['viaje']
			
			#obtener el id de la parada
			
			rutaPar = viaje_parada.objects.filter(id = ultimo).values('rutaParada')
			rupar = rutaPar [0] ['rutaParada']
			
			#obtener la ciudad de la parada, a partir del id de la parada
			
			ciudadpar = ruta_parada.objects.filter(id = rupar).values('parada')
			cpar = viajp [0] ['parada']
			
			#obtener las reservaciones del viaje con destino en la ciudad de la parada y que hayan abordado
			
			personas = reservaciones.objects.filter(viaje = vp).filter(destino = cpar).filter(status=True).count()
			
			#contador actual del camion
			
			conta = viaje.objects.filter(id=vp).values('contados')
			cont = cont [0] ['contados']
			
			#resta del contador menos las personas que acaban de bajar

			cont = cont - personas
			
			#commits 
			#NO TERMINADO
			
			return HttpResponseRedirect('/cuentas')
	else:
		formulario = paradaForm()
	return render_to_response('camionera/Fparada.html',{'formulario':formulario}, context_instance = RequestContext(request))

	
def formAbordar(request):
	if request.method == 'POST':
		formulario = abordarForm(request.POST)
		if formulario.is_valid():
			formulario.save(commit=False)
			
			ultimo = abordar.objects.all().count()
			
			#ultima reservacion en abordar
			
			ultimareservabord = abordar.objects.filter(id = ultimo).values('reservacion')
			ura = ultimareservabord [0] ['rservacion']
			
			#buscar reservacion y actualizar status y agregar fecha abordar
			
			buscarreserv = reservacion.objects.filter(id = ura).update(status = True).update(fechaAbordar = datetime.now)
			
			#buscar el viaje por medio de la reservacion
			
			viaje = reservacion.objects.filter(id = ultimo).values('viaje')
			vi = viaje [0] ['viaje']
			
			#buscar el contador del viaje y sumar 1
			conta = viaje.objects.filter(id=vi).values('contados')
			cont = cont [0] ['contados']
			
			cont = cont +1
			
			#commit 
			#NO TERMINADO
						
			return HttpResponseRedirect('/cuentas')
	else:
		formulario = abordarForm()
	return render_to_response('camionera/Fabordar.html',{'formulario':formulario}, context_instance = RequestContext(request))
