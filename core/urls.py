from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('obras/', views.obra_lista, name='obra_lista'),
    path('obras/criar/', views.obra_criar, name='obra_criar'),
    path('obras/<int:pk>/', views.obra_detalhe, name='obra_detalhe'),
    path('obras/<int:pk>/editar/', views.obra_editar, name='obra_editar'),
    path('obras/<int:pk>/deletar/', views.obra_deletar, name='obra_deletar'),
    path('obras/<int:pk>/progresso/', views.progresso_atualizar, name='progresso_atualizar'),
]
