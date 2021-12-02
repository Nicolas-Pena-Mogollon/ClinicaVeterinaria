from ClinicaVeterinariaApp.serializers import ProductoSerializer


class ProductoService:

    def guardarProducto(self, producto_data):
        producto_serializer = ProductoSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return "se ha registrado correctamente"

        return "Fallo al registrar, los campos ingresados no son correctos!"
