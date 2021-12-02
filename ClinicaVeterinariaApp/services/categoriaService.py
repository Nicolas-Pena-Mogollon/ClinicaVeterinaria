from ClinicaVeterinariaApp.models import Categoria
from ClinicaVeterinariaApp.serializers import CategoriaSerializer


class CategoriaService:

    def crearCategoria(self, categoria_data):
        categoria_serializer = CategoriaSerializer(data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return "se ha registrado correctamente"
        return "Fallo al registrar, los campos ingresados no son correctos!"

    def obtenerCategorias(self):
        try:
            categorias = Categoria.objects.filter(est_categoria="A")
            return CategoriaSerializer(categorias, many=True).data
        except Categoria.DoesNotExist:
            return "No existen categorias"
