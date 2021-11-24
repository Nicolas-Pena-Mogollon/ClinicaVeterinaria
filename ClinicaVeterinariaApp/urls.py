from django.conf.urls import url

from ClinicaVeterinariaApp import views

urlpatterns = [
    url(r'^usuario$', views.usuarioAPI),
    url(r'^rol/', views.rolAPI),
    url(r'^rol$', views.rolAPI),
]
