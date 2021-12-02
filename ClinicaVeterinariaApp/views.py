from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from ClinicaVeterinariaApp.services.adminService import AdminService
from ClinicaVeterinariaApp.services.categoriaService import CategoriaService
from ClinicaVeterinariaApp.services.colorService import ColorService
from ClinicaVeterinariaApp.services.especializacionService import EspecializacionService
from ClinicaVeterinariaApp.services.especieService import EspecieService
from ClinicaVeterinariaApp.services.mascotaService import MascotaService
from ClinicaVeterinariaApp.services.medioPagoService import MedPagoService
from ClinicaVeterinariaApp.services.productoService import ProductoService
from ClinicaVeterinariaApp.services.razaService import RazaService
from ClinicaVeterinariaApp.services.usuarioService import UsuarioService
from ClinicaVeterinariaApp.services.vetService import VetService


@csrf_exempt
def usuariosAPI(request):
    if request.method == 'GET':
        return JsonResponse(UsuarioService().validarLoginUsuario(request), safe=False)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        return JsonResponse(UsuarioService().guardarUsuario(usuario_data), safe=False)


@csrf_exempt
def adminAPI(request):
    if request.method == 'GET':
        return JsonResponse(AdminService().listarVeterniarios(), safe=False)
    elif request.method == 'PUT':
        vet_data = JSONParser().parse(request)
        return JsonResponse(AdminService().eliminarVeterinario(vet_data), safe=False)


@csrf_exempt
def especializacionAPI(request):
    if request.method == 'GET':
        return JsonResponse(EspecializacionService().obtenerEspecializaciones(), safe=False)
    elif request.method == "POST":
        esp_data = JSONParser().parse(request)
        return JsonResponse(EspecializacionService().crearEspecializacion(esp_data), safe=False)


@csrf_exempt
def medPagoAPI(request):
    if request.method == "POST":
        med_pago_data = JSONParser().parse(request)
        return JsonResponse(MedPagoService().crearMedioPago(med_pago_data), safe=False)


@csrf_exempt
def colorAPI(request):
    if request.method == 'GET':
        return JsonResponse(ColorService().obtenerColores(), safe=False)
    elif request.method == "POST":
        color_data = JSONParser().parse(request)
        return JsonResponse(ColorService().crearColor(color_data), safe=False)


@csrf_exempt
def categoriaAPI(request):
    if request.method == 'GET':
        return JsonResponse(CategoriaService().obtenerCategorias(), safe=False)
    elif request.method == "POST":
        categoria_data = JSONParser().parse(request)
        return JsonResponse(CategoriaService().crearCategoria(categoria_data), safe=False)


@csrf_exempt
def especieAPI(request):
    if request.method == 'GET':
        return JsonResponse(EspecieService().obtenerEspecies(), safe=False)
    elif request.method == "POST":
        especie_data = JSONParser().parse(request)
        return JsonResponse(EspecieService().crearEspecie(especie_data), safe=False)


@csrf_exempt
def veterinariaAPI(request, vet_username):
    if request.method == 'GET':
        return JsonResponse(VetService().buscarEspecializaciones(vet_username), safe=False)
    if request.method == 'POST':
        cod_esp = JSONParser().parse(request)['cod_esp']
        return JsonResponse(VetService().asociarEspecializacion(cod_esp, vet_username), safe=False)
    if request.method == 'DELETE':
        return JsonResponse(VetService().desasociarEspecializacion(request.GET['cod_esp'], vet_username), safe=False)


@csrf_exempt
def macotasAPI(request):
    if request.method == 'POST':
        mascota_data = JSONParser().parse(request)
        return JsonResponse(MascotaService().guardarMascota(mascota_data), safe=False)


@csrf_exempt
def razaAPI(request):
    if request.method == 'GET':
        return JsonResponse(RazaService().obtenerRazas(request.GET['cod_especie']), safe=False)
    elif request.method == 'POST':
        raza_data = JSONParser().parse(request)
        return JsonResponse(RazaService().guardarRaza(raza_data), safe=False)


@csrf_exempt
def productoAPI(request):
    if request.method == 'POST':
        producto_data = JSONParser().parse(request)
        return JsonResponse(ProductoService().guardarProducto(producto_data), safe=False)
