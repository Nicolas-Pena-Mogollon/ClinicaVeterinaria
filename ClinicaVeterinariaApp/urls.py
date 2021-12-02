from django.conf.urls import url

from ClinicaVeterinariaApp import views

urlpatterns = [
    url(r'^usuarios$', views.usuariosAPI),
    url(r'^mascotas$', views.macotasAPI),
    url(r'^admin$', views.adminAPI),
    url(r'^especializacion$', views.especializacionAPI),
    url(r'^veterinaria/(?P<vet_username>\w{0,20})/?$', views.veterinariaAPI),
    url(r'^mediopago$', views.medPagoAPI),
    url(r'^color$', views.colorAPI),
    url(r'^categoria$', views.categoriaAPI),
    url(r'^especie$', views.especieAPI),
    url(r'^raza$', views.razaAPI),
    url(r'^producto$', views.productoAPI),

]
