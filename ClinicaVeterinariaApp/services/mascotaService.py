from ClinicaVeterinariaApp.models import Usuario
from ClinicaVeterinariaApp.serializers import MascotaSerializer


class MascotaService:

    def guardarMascota(self, mascota_data):

        try:
            Usuario.objects.filter(username=mascota_data['cod_usuario'], est_usuario="A")
        except Usuario.DoesNotExist:
            return "No existe el usuario!"

        mascota_serializer = MascotaSerializer(data=mascota_data)
        if mascota_serializer.is_valid():
            mascota_serializer.save()
            return "se ha registrado correctamente"
        return "Fallo al registrar, los campos ingresados no son correctos!"
