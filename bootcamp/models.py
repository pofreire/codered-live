from django.db import models
from core.models import Events
from tinymce.models import HTMLField
import datetime


class Artigo(models.Model):
    artigo_id = models.AutoField(primary_key=True)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, default=None)
    bootcamp = models.ForeignKey('Bootcamp', on_delete=models.CASCADE, default=None)
    em_exibicao = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Artigos Bootcamp"

class Bootcamp(Events):
    bootcamp_id = models.AutoField(primary_key=True)
    programacao_bootcamp = HTMLField()
    valor_bootcamp = models.FloatField()


    class Meta:
        verbose_name_plural = "Bootcamps"

    def __str__(self):
        return self.titulo_evento

class Professor(models.Model):
    professor_id = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=150)
    professor_foto = models.FileField(upload_to='static/images', null=True, blank=True)
    descricao_professor = HTMLField(default=None)
    twitter = models.CharField(max_length=150, default=None, blank=True)
    facebook = models.CharField(max_length=150, default=None, blank=True)
    github = models.CharField(max_length=150, default=None, blank=True)
    linkedin = models.CharField(max_length=150, default=None, blank=True)
    titulo = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Professores"

    def __str__(self):
        return self.nome_professor
