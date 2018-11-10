from django.db import models
from core.models import Events
from tinymce.models import HTMLField
import datetime

class Artigo_codedojo(models.Model):
    artigo_codedojo_id = models.AutoField(primary_key=True)
    code_dojo = models.ForeignKey('Code_dojo', on_delete=models.CASCADE, default=None)
    em_exibicao = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Artigos CodeDojo"

class Code_dojo(Events):
    codedojo_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.titulo_evento

    class Meta:
        verbose_name_plural = "CodeDojo"
