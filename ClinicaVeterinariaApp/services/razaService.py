from ClinicaVeterinariaApp.models import Raza
from ClinicaVeterinariaApp.serializers import RazaSerializer


class RazaService:

    def guardarRaza(self, raza_data):
        raza_serializer = RazaSerializer(data=raza_data)
        if raza_serializer.is_valid():
            raza_serializer.save()
            return "se ha registrado correctamente"

        return "Fallo al registrar, los campos ingresados no son correctos!"

    def obtenerRazas(self, cod_especie):
        try:
            razas = Raza.objects.filter(est_raza="A", cod_especie=cod_especie)
            return RazaSerializer(razas, many=True).data
        except Raza.DoesNotExist:
            return "No existen razas"
