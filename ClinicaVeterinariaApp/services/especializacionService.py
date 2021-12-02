from ClinicaVeterinariaApp.models import Especializacion
from ClinicaVeterinariaApp.serializers import EspecializacionSerializer


class EspecializacionService:

    def crearEspecializacion(self, esp_data):

        esp_serializer = EspecializacionSerializer(data=esp_data)
        if esp_serializer.is_valid():
            esp_serializer.save()
            return "se ha registrado correctamente"
        return "Fallo al registrar, los campos ingresados no son correctos!"

    def obtenerEspecializaciones(self):
        try:
            especializaciones = Especializacion.objects.filter(est_especializacion="A")
            return EspecializacionSerializer(especializaciones, many=True).data
        except Especializacion.DoesNotExist:
            return "No existen especializaciones"
