from django.contrib import admin
from .models import Genero, Obra, ProgressoLeitura, HistoricoLeitura, Favorito


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


class ProgressoInline(admin.StackedInline):
    model = ProgressoLeitura
    extra = 0


@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'autor', 'status_obra', 'created_at']
    list_filter = ['tipo', 'status_obra']
    search_fields = ['titulo', 'autor']
    filter_horizontal = ['generos']
    inlines = [ProgressoInline]


@admin.register(ProgressoLeitura)
class ProgressoLeituraAdmin(admin.ModelAdmin):
    list_display = ['obra', 'capitulo_atual', 'pagina_atual', 'status_leitura', 'ultimo_acesso']
    list_filter = ['status_leitura']


@admin.register(HistoricoLeitura)
class HistoricoLeituraAdmin(admin.ModelAdmin):
    list_display = ['obra', 'capitulo', 'pagina', 'lido_em']
    list_filter = ['obra']


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'url', 'icone', 'ordem']
    list_editable = ['ordem']
    search_fields = ['titulo', 'url']
