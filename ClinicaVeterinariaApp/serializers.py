from rest_framework import serializers
from ClinicaVeterinariaApp.models import Usuario, Rol, Especializacion, Especie, Factura, Color, Mascota, Mediopago, \
    Categoria, Producto, Raza, Venta


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('cod_rol', 'descripcion', 'est_rol')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'username', 'clave', 'email', 'num_identificacion', 'nombres', 'apellidos', 'cod_rol', 'direccion',
            'tel_fijo', 'tel_celular', 'est_usuario'
        )

    def to_representation(self, instance):
        self.fields['cod_rol'] = RolSerializer(read_only=True)
        return super(UsuarioSerializer, self).to_representation(instance)


class EspecializacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especializacion
        fields = ('__all__')


class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ('__all__')


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('__all__')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('__all__')


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('__all__')


class MediopagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mediopago
        fields = ('__all__')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ('__all__')


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ('__all__')


