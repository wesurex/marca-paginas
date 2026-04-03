from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Obra, ProgressoLeitura, HistoricoLeitura
from .forms import ObraForm, ProgressoForm


def index(request):
    obras_lendo = Obra.objects.filter(progresso__status_leitura='lendo').select_related('progresso').order_by('-progresso__ultimo_acesso')
    obras_pausadas = Obra.objects.filter(progresso__status_leitura='pausado').select_related('progresso').order_by('-progresso__ultimo_acesso')
    return render(request, 'core/index.html', {
        'obras_lendo': obras_lendo,
        'obras_pausadas': obras_pausadas,
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
