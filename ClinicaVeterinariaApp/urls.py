from django.conf.urls import url

from ClinicaVeterinariaApp import views

urlpatterns = [
    url(r'^usuarios$', views.usuariosAPI),
    url(r'^rol$', views.rolAPI),
]
