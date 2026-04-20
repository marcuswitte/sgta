from django.urls import path
from .views import (
    listar_usuario,
    buscar_usuario_por_id,
)

urlpatterns = [
    path('usuarios/', listar_usuario),
    path('usuarios/<int:id>/', buscar_usuario_por_id),
]