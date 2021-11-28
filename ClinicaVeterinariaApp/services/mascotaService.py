from ClinicaVeterinariaApp.serializers import MascotaSerializer


class MascotaService:

    def guardarMascota(self, mascota_data):

        mascota_serializer = MascotaSerializer(data=mascota_data)
        if mascota_serializer.is_valid():
            mascota_serializer.save()
            return "se ha registrado correctamente"

        return "Fallo al registrar, los campos ingresados no son correctos!"