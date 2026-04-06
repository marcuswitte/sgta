from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer
from django.http import JsonResponse
from django.utils import timezone

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    """Lista somente as tarefas com status ABERTA"""
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

# Exercício 2 — Listar tarefas por prioridade
def listar_tarefas_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)

# Exercício 3 — Buscar tarefa por id
def buscar_tarefa_por_id(request, id):
    try:
        tarefa = Tarefa.objects.filter(id=id).values().get()
        return JsonResponse(tarefa)
    except Tarefa.DoesNotExist:
        return JsonResponse({'erro': 'Tarefa não encontrada.'}, status=404)

# Exercício 4 — Listar tarefas ABERTA e URGENTE
def listar_tarefas_abertas_urgentes(request):
    tarefas = Tarefa.objects.filter(status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

# Exercício 5 — Listar tarefas atrasadas (data_entrega < hoje e não CONCLUIDA)
def listar_tarefas_atrasadas(request):
    hoje = timezone.now().date()
    tarefas = Tarefa.objects.filter(data_entrega__lt=hoje).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

# Exercício 6 — Buscar tarefas por palavra no título
def buscar_tarefas_por_titulo(request, palavra):
    tarefas = Tarefa.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefas), safe=False)

class TarefaAbertaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tarefa.objects.filter(status='ABERTA')
    serializer_class = TarefaSerializer
