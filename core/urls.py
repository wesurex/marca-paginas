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

    # AJAX
    path('ajax/obras/search/', views.obra_search_ajax, name='obra_search_ajax'),
    path('ajax/obras/<int:pk>/toggle-favorito/', views.obra_toggle_favorito, name='obra_toggle_favorito'),

    # Favoritos
    path('favoritos/', views.favorito_lista, name='favorito_lista'),
    path('favoritos/criar/', views.favorito_criar, name='favorito_criar'),
    path('favoritos/<int:pk>/editar/', views.favorito_editar, name='favorito_editar'),
    path('favoritos/<int:pk>/deletar/', views.favorito_deletar, name='favorito_deletar'),
    path('favoritos/reordenar/', views.favorito_reordenar, name='favorito_reordenar'),
]
