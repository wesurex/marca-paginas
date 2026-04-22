from django import forms
from .models import Obra, ProgressoLeitura, Genero, Favorito


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'tipo', 'capa', 'capa_url', 'site_base_url', 'total_capitulos', 'status_obra', 'classificacao', 'descricao', 'notas']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Berserk'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'capa': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'capa_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://... (opcional, se não fizer upload)'}),
            'site_base_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'total_capitulos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Deixe vazio se não souber'}),
            'status_obra': forms.Select(attrs={'class': 'form-select'}),
            'classificacao': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Sinopse ou descrição da obra...'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Suas anotações pessoais sobre a obra...'}),
        }


class ProgressoForm(forms.ModelForm):
    class Meta:
        model = ProgressoLeitura
        fields = ['capitulo_atual', 'pagina_atual', 'url_atual', 'status_leitura', 'notas']
        widgets = {
            'capitulo_atual': forms.NumberInput(attrs={'class': 'form-control'}),
            'pagina_atual': forms.NumberInput(attrs={'class': 'form-control'}),
            'url_atual': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'status_leitura': forms.Select(attrs={'class': 'form-select'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Anotações sobre onde parou, próximo arco, etc.'}),
        }


class FavoritoForm(forms.ModelForm):
    class Meta:
        model = Favorito
        fields = ['titulo', 'url', 'descricao', 'icone']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: MangaDex'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Descrição breve (opcional)'}),
            'icone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: bi-book, bi-github'}),
        }
