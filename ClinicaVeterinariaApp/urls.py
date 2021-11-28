from django.conf.urls import url

from ClinicaVeterinariaApp import views

urlpatterns = [
    url(r'^usuarios$', views.usuariosAPI),
    url(r'^usuarios/{username}/mascotas$', views.macotasAPI),
    url(r'^admin$', views.adminAPI)
]
'''url(r'^rol$', views.rolAPI),'''
""",
    url(r'^admin/(?P<username>\w{0,20})/$', views.adminAPI)"""