from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from .forms import VacanteForm, VacacionesForm
from .models import Vacante, Vacaciones

# Create your views here.

def home(request):
	try:
		del request.session['user']
	except KeyError:
		pass
	return render(request, 'home.html', )

def vacante(request):
	if(not request.session.get('user', False)):
		return HttpResponseRedirect('/fase1/')

	if(request.session['user'] == 'empleado'):
		error = False
		if(request.method == "POST"):
			form = VacanteForm(request.POST)
			if(form.is_valid()):
				form.save()
				return HttpResponseRedirect('/fase1/')
			else:
				error = True
		else:
			form = VacanteForm()

		context = {'form': form, 'action': "/fase1/vacante/", 'error': error}
		
		return render(request, 'formulario.html', context)

	else:
		if(request.method == "DELETE"):
			params = QueryDict(request.body)
			v = get_object_or_404(Vacante, id=params.get('id'))
			v.delete()
			return HttpResponse("Success")

		v = Vacante.objects.all()
		context = {'solicitudes': v, 'vacante': True}
		return render(request, 'listado.html', context)

def vacaciones(request):
	if(not request.session.get('user', False)):
		return HttpResponseRedirect('/fase1/')

	if(request.session['user'] == 'empleado'):
		error = False
		if(request.method == "POST"):
			form = VacacionesForm(request.POST)
			if(form.is_valid()):
				form.save()
				return HttpResponseRedirect('/fase1/')
			else:
				error = True
		else:
			form = VacacionesForm()
		
		context = {'form': form, 'action': "/fase1/vacaciones/", 'error': error}

		return render(request, 'formulario.html', context)

	else:
		if(request.method == "DELETE"):
			params = QueryDict(request.body)
			v = get_object_or_404(Vacaciones, id=params.get('id'))
			v.delete()
			return HttpResponse("Success")

		v = Vacaciones.objects.all()
		context = {'solicitudes': v, 'vacaciones': True}
		return render(request, 'listado.html', context)

def empleado(request):
	request.session['user'] = 'empleado'
	return HttpResponseRedirect('/fase1/vacante')

def hhrr(request):
	request.session['user'] = 'hhrr'
	return HttpResponseRedirect('/fase1/vacante')
