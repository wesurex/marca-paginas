from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['nome']


class Obra(models.Model):
    TIPO_CHOICES = [
        ('livro', 'Livro'),
        ('manga', 'Manga'),
        ('manhwa', 'Manhwa'),
        ('manhua', 'Manhua'),
    ]
    STATUS_OBRA_CHOICES = [
        ('em_andamento', 'Em andamento'),
        ('completo', 'Completo'),
        ('hiato', 'Hiato'),
        ('cancelado', 'Cancelado'),
    ]

    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    autor = models.CharField(max_length=255, blank=True)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True, verbose_name='Imagem da capa')
    capa_url = models.URLField(blank=True, verbose_name='URL da capa (alternativa)')
    site_base_url = models.URLField(blank=True, verbose_name='URL do site')
    total_capitulos = models.PositiveIntegerField(null=True, blank=True, verbose_name='Total de capítulos')
    status_obra = models.CharField(max_length=20, choices=STATUS_OBRA_CHOICES, default='em_andamento', verbose_name='Status da obra')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    notas = models.TextField(blank=True, verbose_name='Notas pessoais')
    classificacao = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Classificação',
        choices=[(i, f'{i}/10') for i in range(1, 11)])
    generos = models.ManyToManyField(Genero, blank=True, verbose_name='Gêneros')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering = ['titulo']


class ProgressoLeitura(models.Model):
    STATUS_LEITURA_CHOICES = [
        ('lendo', 'Lendo'),
        ('pausado', 'Pausado'),
        ('completo', 'Completo'),
        ('abandonado', 'Abandonado'),
    ]

    obra = models.OneToOneField(Obra, on_delete=models.CASCADE, related_name='progresso')
    capitulo_atual = models.PositiveIntegerField(default=1, verbose_name='Capítulo atual')
    pagina_atual = models.PositiveIntegerField(default=1, verbose_name='Página atual')
    url_atual = models.URLField(blank=True, verbose_name='URL atual')
    status_leitura = models.CharField(max_length=20, choices=STATUS_LEITURA_CHOICES, default='lendo', verbose_name='Status de leitura')
    notas = models.TextField(blank=True, verbose_name='Notas')
    ultimo_acesso = models.DateTimeField(auto_now=True, verbose_name='Último acesso')

    def __str__(self):
        return f'Progresso — {self.obra.titulo}'

    class Meta:
        verbose_name = 'Progresso de Leitura'
        verbose_name_plural = 'Progressos de Leitura'


class HistoricoLeitura(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='historico')
    capitulo = models.PositiveIntegerField(verbose_name='Capítulo')
    pagina = models.PositiveIntegerField(default=1, verbose_name='Página')
    url_acessada = models.URLField(blank=True, verbose_name='URL acessada')
    lido_em = models.DateTimeField(auto_now_add=True, verbose_name='Lido em')

    def __str__(self):
        return f'{self.obra.titulo} — Cap. {self.capitulo}'

    class Meta:
        verbose_name = 'Histórico de Leitura'
        verbose_name_plural = 'Histórico de Leituras'
        ordering = ['-lido_em']
