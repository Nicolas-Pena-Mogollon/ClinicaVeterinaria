import base64

import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from ClinicaVeterinariaApp.models import Usuario, Rol
from ClinicaVeterinariaApp.serializers import UsuarioSerializer, RolSerializer

# Create your views here.
from ClinicaVeterinariaApp.services.usuarioService import UsuarioService


@csrf_exempt
def usuariosAPI(request):
    if request.method == 'GET':
        return JsonResponse(UsuarioService().validarLoginUsuario(request), safe=False)

    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        return JsonResponse(UsuarioService().guardarUsuario(usuario_data), safe=False)
    elif request.method == 'PUT':
        print("Actualizar")
    elif request.method == 'DELETE':
        print("eliminar")


@csrf_exempt
def rolAPI(request):
    if request.method == 'GET':
        print(request)
        roles = Rol.objects.raw('SELECT * FROM rol')
        rol_serializer = RolSerializer(roles, many=True)
        print(rol_serializer.data)
        return JsonResponse(rol_serializer.data, safe=False)
    elif request.method == 'POST':
        rol_data = JSONParser().parse(request)
        rol_serializer = RolSerializer(data=rol_data)
        print(rol_data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return JsonResponse(rol_serializer.data, safe=False)
        return JsonResponse("Fallo al registrar", safe=False)
