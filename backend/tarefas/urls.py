from django.urls import path
from .views import (
    listar_tarefas,
    listar_tarefas_abertas,
    listar_tarefas_por_prioridade,
    buscar_tarefa_por_id,
    listar_tarefas_abertas_urgentes,
    listar_tarefas_atrasadas,
    buscar_tarefas_por_titulo,
)

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas/', listar_tarefas_abertas),
    path('tarefas/prioridade/<str:prioridade>/', listar_tarefas_por_prioridade),   # Ex2
    path('tarefas/abertas/urgentes/', listar_tarefas_abertas_urgentes),            # Ex4
    path('tarefas/atrasadas/', listar_tarefas_atrasadas),                          # Ex5
    path('tarefas/busca/<str:palavra>/', buscar_tarefas_por_titulo),               # Ex6
    path('tarefas/<int:id>/', buscar_tarefa_por_id),                               # Ex3
]