from django.db import models
from tinymce.models import HTMLField
from django.conf import settings

import datetime

class Events(models.Model):
    titulo_evento = models.CharField(max_length=150)
    imagem_evento = models.FileField(upload_to=settings.STATICFILES_DIRS, null=True, blank=True)
    legenda_imagem_evento = models.CharField(max_length=150)
    descricao_evento = HTMLField()
    pre_requisitos_evento = HTMLField()
    prepare_se_evento = HTMLField()
    local_evento = HTMLField()
    carga_horaria_evento = models.IntegerField(default=0)
    data_inicial_evento = models.DateField(default=datetime.date.today)
    data_final_evento = models.DateField(default=datetime.date.today)
    ativo = models.BooleanField(default=False)
    maximo_inscritos = models.IntegerField(default=0)
    inscritos_confirmados = models.IntegerField(default=0)
    inscritos_totais = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def atualiza_curso(self):
        self.inscritos_totais += 1
        self.save()

    def confirma_inscricao(self):
        self.inscritos_totais -= 1
        self.inscritos_confirmados += 1
        self.save()
