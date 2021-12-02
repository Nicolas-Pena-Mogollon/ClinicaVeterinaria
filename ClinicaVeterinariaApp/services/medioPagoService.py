from ClinicaVeterinariaApp.serializers import MediopagoSerializer


class MedPagoService:

    def crearMedioPago(self, medPago_data):
        med_pago_serializer = MediopagoSerializer(data=medPago_data)
        if med_pago_serializer.is_valid():
            med_pago_serializer.save()
            return "se ha registrado correctamente"
        return "Fallo al registrar, los campos ingresados no son correctos!"