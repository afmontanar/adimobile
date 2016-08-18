import json
from django.shortcuts import render

# Create your views here.
from inventario.models import Articulo
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import IntegrityError


def index(request):
	return render_to_response('index.html', {'nothing': 'nothing'})

def guardar_articulo(request):
	if request.is_ajax():
		co = request.GET['co']
		no = request.GET['no']

		try:
			r = Articulo.objects.create(codigo=co, nombre=no)
			return HttpResponse(
			json.dumps({'respuesta': 'si'}),
			content_type="application/json; charset=uft8"
			)
		except IntegrityError:
			return HttpResponse(
			json.dumps({'respuesta': 'no'}),
			content_type="application/json; charset=uft8"
			)