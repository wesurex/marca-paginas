from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q, Max
import json
from .models import Obra, ProgressoLeitura, HistoricoLeitura, Favorito
from .forms import ObraForm, ProgressoForm, FavoritoForm


def index(request):
    obras_favoritas = Obra.objects.filter(favorito=True).select_related('progresso').order_by('-updated_at')
    obras_lendo = Obra.objects.filter(progresso__status_leitura='lendo').select_related('progresso').order_by('-progresso__ultimo_acesso')
    obras_pausadas = Obra.objects.filter(progresso__status_leitura='pausado').select_related('progresso').order_by('-progresso__ultimo_acesso')
    favoritos = Favorito.objects.all()
    return render(request, 'core/index.html', {
        'obras_favoritas': obras_favoritas,
        'obras_lendo': obras_lendo,
        'obras_pausadas': obras_pausadas,
        'favoritos': favoritos,
    })


def obra_lista(request):
    obras = Obra.objects.all().prefetch_related('generos').select_related('progresso')
    tipo_filtro = request.GET.get('tipo', '')
    status_filtro = request.GET.get('status', '')
    if tipo_filtro:
        obras = obras.filter(tipo=tipo_filtro)
    if status_filtro:
        obras = obras.filter(progresso__status_leitura=status_filtro)
    return render(request, 'core/obras/lista.html', {
        'obras': obras,
        'tipo_filtro': tipo_filtro,
        'status_filtro': status_filtro,
        'tipo_choices': Obra.TIPO_CHOICES,
        'status_choices': ProgressoLeitura.STATUS_LEITURA_CHOICES,
    })


def obra_detalhe(request, pk):
    obra = get_object_or_404(Obra.objects.prefetch_related('generos'), pk=pk)
    historico = obra.historico.all()[:15]
    return render(request, 'core/obras/detalhe.html', {
        'obra': obra,
        'historico': historico,
    })


def obra_criar(request):
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            obra = form.save()
            ProgressoLeitura.objects.create(obra=obra)
            messages.success(request, f'"{obra.titulo}" cadastrado com sucesso!')
            return redirect('obra_detalhe', pk=obra.pk)
    else:
        form = ObraForm()
    return render(request, 'core/obras/form.html', {'form': form, 'titulo_pagina': 'Cadastrar Obra'})


def obra_editar(request, pk):
    obra = get_object_or_404(Obra, pk=pk)
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{obra.titulo}" atualizado com sucesso!')
            return redirect('obra_detalhe', pk=obra.pk)
    else:
        form = ObraForm(instance=obra)
    return render(request, 'core/obras/form.html', {
        'form': form,
        'titulo_pagina': 'Editar Obra',
        'obra': obra,
    })


def obra_deletar(request, pk):
    obra = get_object_or_404(Obra, pk=pk)
    if request.method == 'POST':
        titulo = obra.titulo
        obra.delete()
        messages.success(request, f'"{titulo}" removido.')
        return redirect('obra_lista')
    return render(request, 'core/obras/confirmar_delete.html', {'obra': obra})


def progresso_atualizar(request, pk):
    obra = get_object_or_404(Obra, pk=pk)
    progresso = obra.progresso
    capitulo_anterior = progresso.capitulo_atual
    pagina_anterior = progresso.pagina_atual
    url_anterior = progresso.url_atual

    if request.method == 'POST':
        form = ProgressoForm(request.POST, instance=progresso)
        if form.is_valid():
            novo = form.save(commit=False)
            if novo.capitulo_atual != capitulo_anterior:
                HistoricoLeitura.objects.create(
                    obra=obra,
                    capitulo=capitulo_anterior,
                    pagina=pagina_anterior,
                    url_acessada=url_anterior,
                )
            novo.save()
            messages.success(request, 'Progresso atualizado!')
            return redirect('obra_detalhe', pk=obra.pk)
    else:
        form = ProgressoForm(instance=progresso)
    return render(request, 'core/progresso/form.html', {'form': form, 'obra': obra})


# AJAX Search
def obra_search_ajax(request):
    query = request.GET.get('q', '').strip()
    if not query or len(query) < 2:
        return JsonResponse({'obras': []})

    obras = Obra.objects.filter(
        Q(titulo__icontains=query)
    ).select_related('progresso')[:10]

    resultados = []
    for obra in obras:
        capa_url = obra.capa_url if obra.capa_url else (obra.capa.url if obra.capa else '')
        resultados.append({
            'id': obra.pk,
            'titulo': obra.titulo,
            'tipo': obra.get_tipo_display(),
            'autor': obra.autor,
            'capa_url': capa_url,
            'status_leitura': obra.progresso.get_status_leitura_display() if hasattr(obra, 'progresso') else '',
            'capitulo_atual': obra.progresso.capitulo_atual if hasattr(obra, 'progresso') else 1,
            'url_detalhe': f'/obras/{obra.pk}/',
        })

    return JsonResponse({'obras': resultados})


# Favoritos CRUD
def favorito_lista(request):
    favoritos = Favorito.objects.all()
    return render(request, 'core/favoritos/lista.html', {'favoritos': favoritos})


def favorito_criar(request):
    if request.method == 'POST':
        form = FavoritoForm(request.POST)
        if form.is_valid():
            favorito = form.save(commit=False)
            # Definir ordem automaticamente
            max_ordem = Favorito.objects.aggregate(Max('ordem'))['ordem__max']
            favorito.ordem = (max_ordem or 0) + 1
            favorito.save()

            # Retornar JSON se for AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'favorito': {
                        'id': favorito.pk,
                        'titulo': favorito.titulo,
                        'url': favorito.url,
                        'icone': favorito.icone,
                    }
                })

            messages.success(request, f'"{favorito.titulo}" adicionado aos favoritos!')
            return redirect('index')
    else:
        form = FavoritoForm()

    return render(request, 'core/favoritos/form.html', {
        'form': form,
        'titulo_pagina': 'Adicionar Favorito'
    })


def favorito_editar(request, pk):
    favorito = get_object_or_404(Favorito, pk=pk)
    if request.method == 'POST':
        form = FavoritoForm(request.POST, instance=favorito)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{favorito.titulo}" atualizado!')
            return redirect('favorito_lista')
    else:
        form = FavoritoForm(instance=favorito)

    return render(request, 'core/favoritos/form.html', {
        'form': form,
        'titulo_pagina': 'Editar Favorito',
        'favorito': favorito,
    })


def favorito_deletar(request, pk):
    favorito = get_object_or_404(Favorito, pk=pk)
    if request.method == 'POST':
        titulo = favorito.titulo
        favorito.delete()
        messages.success(request, f'"{titulo}" removido dos favoritos.')
        return redirect('favorito_lista')
    return render(request, 'core/favoritos/confirmar_delete.html', {'favorito': favorito})


def favorito_reordenar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ordem = data.get('ordem', [])

            for index, fav_id in enumerate(ordem):
                Favorito.objects.filter(pk=fav_id).update(ordem=index)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    return JsonResponse({'success': False}, status=400)


# Toggle Favorito em Obras
def obra_toggle_favorito(request, pk):
    if request.method == 'POST':
        try:
            obra = get_object_or_404(Obra, pk=pk)
            obra.favorito = not obra.favorito
            obra.save()

            return JsonResponse({
                'success': True,
                'favorito': obra.favorito
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    return JsonResponse({'success': False}, status=400)
