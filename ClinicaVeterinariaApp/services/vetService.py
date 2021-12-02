from ClinicaVeterinariaApp.models import Usuario, Especializacion
from ClinicaVeterinariaApp.serializers import UsuarioSerializer, EspecializacionSerializer


class VetService:

    def asociarEspecializacion(self, cod_esp, vet_id):
        try:
            especializacion = Especializacion.objects.get(cod_esp=cod_esp, est_especializacion="A")
        except Usuario.DoesNotExist:
            return "La especialización indicada no existe"

        try:
            veterinario = Usuario.objects.get(username=vet_id, cod_rol=3)
            veterinario.usuarioespec.add(especializacion.cod_esp)
            veterinario.save()
            return "Se ha añadido correctamente la especialización"
        except Usuario.DoesNotExist:
            return "No existe un veterinario con ese username"

    def buscarEspecializaciones(self, vet_id):
        try:
            veterinario = Usuario.objects.get(username=vet_id, cod_rol=3)
        except Usuario.DoesNotExist:
            return "No existe un veterinario con ese username"

        especializaciones = EspecializacionSerializer(veterinario.usuarioespec.all(), many=True)
        return especializaciones.data

    def desasociarEspecializacion(self, cod_esp, vet_id):
        try:
            especializacion = Especializacion.objects.get(cod_esp=cod_esp)
        except Usuario.DoesNotExist:
            return "La especialización indicada no existe"

        try:
            veterinario = Usuario.objects.get(username=vet_id, cod_rol=3)
            veterinario.usuarioespec.remove(especializacion.cod_esp)
            veterinario.save()
            return "Se ha removido correctamente la especialización"
        except Usuario.DoesNotExist:
            return "No existe un veterinario con ese username"
