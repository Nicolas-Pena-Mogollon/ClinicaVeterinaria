import base64
import copy

from rest_framework.parsers import JSONParser

from ClinicaVeterinariaApp.models import Usuario
from ClinicaVeterinariaApp.serializers import UsuarioSerializer


class AdminService:

    def listarVeterniarios(self):
        try:
            veterinarios = Usuario.objects.filter(cod_rol="3", est_usuario="A")
        except Usuario.DoesNotExist:
            return "No existen veterinarios"
        veterinarios_serializer = UsuarioSerializer(veterinarios, many=True)
        return veterinarios_serializer.data

    def eliminarVeterinario(self, username):
        try:
            veterinario_act = Usuario.objects.get(username=username)
            veterinario_nue = copy.copy(veterinario_act)
            veterinario_nue.est_usuario = "I"
        except Usuario.DoesNotExist:
            return "No se ha encontrado el veterinario a eliminar"
        veterinario_nue_serializer = UsuarioSerializer(veterinario_nue, many=False)
        json = JSONParser().parse(veterinario_nue_serializer.data)
        json['cod_rol'] = 3
        print(json)
        veterinarios_serializer = UsuarioSerializer(veterinario_act, data=veterinario_nue_serializer.data)
        if veterinarios_serializer.is_valid():
            veterinarios_serializer.save()
            return "Se ha eliminado exitosamente"
        print(veterinarios_serializer.errors)
        return "No se ha encontrado el veterinario a eliminar"
