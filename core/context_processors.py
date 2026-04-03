from .models import ProgressoLeitura


def contadores_leitura(request):
    return {
        'nav_contadores': {
            'lendo':     ProgressoLeitura.objects.filter(status_leitura='lendo').count(),
            'pausado':   ProgressoLeitura.objects.filter(status_leitura='pausado').count(),
            'completo':  ProgressoLeitura.objects.filter(status_leitura='completo').count(),
            'abandonado': ProgressoLeitura.objects.filter(status_leitura='abandonado').count(),
        }
    }
