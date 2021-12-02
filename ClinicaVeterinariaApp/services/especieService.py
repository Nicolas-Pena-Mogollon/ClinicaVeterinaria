from ClinicaVeterinariaApp.models import Especie
from ClinicaVeterinariaApp.serializers import EspecieSerializer


class EspecieService:

    def crearEspecie(self, especie_data):
        especie_serializer = EspecieSerializer(data=especie_data)
        if especie_serializer.is_valid():
            especie_serializer.save()
            return "se ha registrado correctamente"
        return "Fallo al registrar, los campos ingresados no son correctos!"

    def obtenerEspecies(self):
        try:
            especies = Especie.objects.filter(est_especie="A")
            return EspecieSerializer(especies, many=True).data
        except Especie.DoesNotExist:
            return "No existen especies"