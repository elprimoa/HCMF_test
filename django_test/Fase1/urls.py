from django.conf.urls import patterns, url

import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^vacante/$', views.vacante, name='vacante'),
	url(r'^vacaciones/$', views.vacaciones, name='vacaciones'),
	url(r'^empleado/$', views.empleado, name='empleado'),
	url(r'^hhrr/$', views.hhrr, name='hhrr'),
]