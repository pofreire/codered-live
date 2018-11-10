from django.db import models
from tinymce.models import HTMLField

class Integrante_equipe(models.Model):
    integrante_equipe_id = models.AutoField(primary_key=True)
    integrante_nome = models.CharField(max_length=150)
    integrante_foto = models.FileField(upload_to='static/images', null=True, blank=True)
    integrante_cargo = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    facebook = models.CharField(max_length=150)
    github = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Integrantes"

class CodeRed_descricao(models.Model):
    descricao_codered = HTMLField()

    class Meta:
        verbose_name_plural = "Quem Somos"
