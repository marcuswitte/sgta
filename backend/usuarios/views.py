from .models import Usuario
from django.http import JsonResponse

def listar_usuario(request):
    usuario = Usuario.objects.all().values()
    return JsonResponse(list(usuario), safe=False)

def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.filter(id=id).values().get()
        return JsonResponse(usuario)
    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'Usuario nao encontrado.'}, status=404)