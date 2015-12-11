from django.contrib import admin
from .models import Vacante, Vacaciones
from django import forms

# Register your models here.

class VacacionesForm(forms.ModelForm):
	class Meta:
		model = Vacaciones
		exclude = []
	def __init__(self, *args, **kwargs):
		super(VacacionesForm, self).__init__(*args, **kwargs)
	def clean(self):
		cleaned_data = super(VacacionesForm, self).clean()
		start_date = cleaned_data.get("fecha_inicio")
		end_date = cleaned_data.get("fecha_fin")
		if(end_date < start_date):
			raise forms.ValidationError("Fechas invalidas!")
		return self.cleaned_data

class VacacionesAdmin(admin.ModelAdmin):
	form = VacacionesForm

admin.site.register(Vacante)
admin.site.register(Vacaciones, VacacionesAdmin)