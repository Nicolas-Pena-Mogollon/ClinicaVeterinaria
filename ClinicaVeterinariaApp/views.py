from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from ClinicaVeterinariaApp.models import Usuario, Rol
from ClinicaVeterinariaApp.serializers import UsuarioSerializer, RolSerializer


# Create your views here.


@csrf_exempt
def usuarioAPI(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.raw('SELECT * FROM usuario')
        usuario_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuario_serializer.data, safe=True)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        artist = Rol.objects.get(cod_rol=1)
        print(usuario_data)
        usuario_serializer = UsuarioSerializer(data=usuario_data)

        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(request)
        return JsonResponse("Fallo al registrar", safe=False)
    elif request.method == 'PUT':
        print("Actualizar")
    elif request.method == 'DELETE':
        print("eliminar")


@csrf_exempt
def rolAPI(request):
    if request.method == 'GET':
        print("hola")
        roles = Rol.objects.raw('SELECT * FROM rol')
        rol_serializer = RolSerializer(roles, many=True)
        print(rol_serializer.data)
        return JsonResponse(rol_serializer.data, safe=False)
