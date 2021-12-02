from ClinicaVeterinariaApp.models import Color
from ClinicaVeterinariaApp.serializers import ColorSerializer


class ColorService:

    def crearColor(self, color_data):
        color_serializer = ColorSerializer(data=color_data)
        if color_serializer.is_valid():
            color_serializer.save()
            return "se ha registrado correctamente"
        return "Fallo al registrar, los campos ingresados no son correctos!"

    def obtenerColores(self):
        try:
            colores = Color.objects.filter(est_color="A")
            return ColorSerializer(colores, many=True).data
        except Color.DoesNotExist:
            return "No existen colores"
