from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import F

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values('id', 'titulo', 'status', 'prioridade', 'usuario_responsavel_id', usuario_nome=F('usuario_responsavel__nome'))
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefa_por_id(request, id):
    try:
        tarefa = Tarefa.objects.filter(id=id).values().get()
        return JsonResponse(tarefa)
    except Tarefa.DoesNotExist:
        return JsonResponse({'erro': 'Tarefa nao encontrada.'}, status=404)

def listar_tarefas_abertas_urgentes(request):
    tarefas = Tarefa.objects.filter(status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_atrasadas(request):
    hoje = timezone.now().date()
    tarefas = Tarefa.objects.filter(data_entrega__lt=hoje).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefas_por_titulo(request, palavra):
    tarefas = Tarefa.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefas), safe=False)

class TarefaAbertaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tarefa.objects.filter(status='ABERTA')
    serializer_class = TarefaSerializer
