from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer
from django.http import JsonResponse

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    """Lista somente as tarefas com status ABERTA"""
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

class TarefaAbertaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tarefa.objects.filter(status='ABERTA')
    serializer_class = TarefaSerializer
