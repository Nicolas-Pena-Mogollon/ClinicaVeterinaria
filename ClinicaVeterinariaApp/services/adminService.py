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

    def eliminarVeterinario(self, vet_data):
        try:
            veterinario = Usuario.objects.get(username=vet_data['username'])
            veterinarios_serializer = UsuarioSerializer(veterinario, data=vet_data)

        except Usuario.DoesNotExist:
            return "No se ha encontrado el veterinario a eliminar"

        if veterinarios_serializer.is_valid():
            veterinarios_serializer.save()
            return "Se ha eliminado exitosamente"
        return "No se ha encontrado el veterinario a eliminar"
