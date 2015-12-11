from django import forms
from .models import Vacante, Vacaciones

class VacanteForm(forms.ModelForm):
	class Meta:
		model = Vacante
		exclude = ['fecha_creacion', 'reclutador']
	def __init__(self, *args, **kwargs):
		super(VacanteForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class VacacionesForm(forms.ModelForm):
	class Meta:
		model = Vacaciones
		exclude = ['fecha_creacion']
	def __init__(self, *args, **kwargs):
		super(VacacionesForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
		self.fields['fecha_inicio'].widget.attrs.update({
			'id': 'from',
			'readonly': True
		})
		self.fields['fecha_fin'].widget.attrs.update({
			'id': 'to',
			'readonly': True
		})
	def clean(self):
		cleaned_data = super(VacacionesForm, self).clean()
		start_date = cleaned_data.get("fecha_inicio")
		end_date = cleaned_data.get("fecha_fin")
		if(end_date < start_date):
			raise forms.ValidationError("Fechas invalidas!")
		return self.cleaned_data
