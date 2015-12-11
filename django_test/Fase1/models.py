from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.

class Vacante(models.Model):
	cargo = models.CharField(max_length = 1024, default = "")
	vacantes = models.IntegerField(default = 0)
	TIPO_CARGO_CHOICE = (('N', 'Nuevo'), ('R', 'Reemplazo'))
	tipo_cargo = models.CharField(max_length = 1, choices = TIPO_CARGO_CHOICE, default = 'N')
	TIPO_JORNADA_CHOICE = (('P', 'Part-time'), ('F', 'Full-time'))
	tipo_jornada = models.CharField(max_length = 1, choices = TIPO_JORNADA_CHOICE, default = 'P')
	sueldo = models.FloatField(default = 0)
	comentarios = models.TextField(default = "", blank = True)
	fecha_creacion = models.DateField(default = date.today)
	solicitante = models.CharField(max_length = 1024, default = "")
	receptor = models.CharField(max_length = 1024, default = "")
	def __str__(self):
		return "Solicitud de " + self.solicitante

class Vacaciones(models.Model):
	fecha_inicio = models.DateField(default = date.today)
	fecha_fin = models.DateField(default = date.today)
	motivo = models.TextField(default = "")
	fecha_creacion = models.DateField(default = date.today)
	solicitante = models.CharField(max_length = 1024, default = "")
	receptor = models.CharField(max_length = 1024, default = "")
	def __str__(self):
		return "Solicitud de " + self.solicitante
