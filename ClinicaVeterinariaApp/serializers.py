from rest_framework import serializers
from ClinicaVeterinariaApp.models import Usuario, Rol


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('cod_rol', 'descripcion', 'est_rol')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'username', 'clave', 'email', 'num_identificacion', 'nombres', 'apellidos', 'cod_rol', 'direccion',
            'tel_fijo',
            'tel_celular', 'est_usuario'
        )
