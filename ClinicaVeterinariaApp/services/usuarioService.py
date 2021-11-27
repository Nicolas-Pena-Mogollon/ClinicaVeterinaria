import base64

from ClinicaVeterinariaApp.models import Usuario
from ClinicaVeterinariaApp.serializers import UsuarioSerializer



class UsuarioService:

    def guardarUsuario(self, usuario_data):

        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return "se ha registrado correctamente"

        usuario = Usuario.objects.get(username=usuario_serializer.data['username'])
        if usuario:
            return "Ya se encuentra registrado un usuario con este username!"

        return "Fallo al registrar, los campos ingresados no son correctos!"

    def validarLoginUsuario(self, request_data):
        auth_headers = request_data.headers['Authorization'].replace("Basic ", "")
        credenciales = str(base64.b64decode(auth_headers)).replace("b'", "").replace("'", "").split(":")

        try:
            usuario = Usuario.objects.get(username=credenciales[0])
        except Usuario.DoesNotExist:
            usuario = None

        if usuario:
            if usuario.clave == credenciales[1]:
                print(usuario.cod_rol.descripcion)
                return usuario.cod_rol.descripcion
            return "Contraseña incorrecta!"
        return "Nombre de usuario incorrecto!"
