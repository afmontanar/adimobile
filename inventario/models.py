from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Articulo(models.Model):
	codigo = models.CharField(max_length=30, primary_key=True)
	nombre = models.CharField(max_length=200)
	tipocodigo = models.CharField(max_length=1, null=True)
	localizacion = models.CharField(max_length=30, null=True)
	existenciamax = models.CharField(max_length=30, null=True)
	referecia = models.CharField(max_length=30, null=True)
	dependencia = models.CharField(max_length=30, null=True)
	existenciamin = models.CharField(max_length=30, null=True)
	descripcionapida = models.CharField(max_length=30, null=True)
	estado = models.CharField(max_length=30, null=True)
	fletes = models.CharField(max_length=30, null=True)
	costoventa = models.CharField(max_length=30, null=True)
	costobase = models.CharField(max_length=30, null=True)
	tipoarticulo = models.CharField(max_length=30, null=True)
	preciovent1 = models.CharField(max_length=30, null=True)
	tipoempaque = models.CharField(max_length=30, null=True)
	preciovent2 = models.CharField(max_length=30, null=True)
	preciovent3 = models.CharField(max_length=30, null=True)
	dtofacturacion = models.CharField(max_length=30, null=True)
	lote = models.CharField(max_length=30, null=True)

	def __unicode__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('clientes', kwargs={'pk':self.pk})

