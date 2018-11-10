from django.db import models
from bootcamp.models import Bootcamp
from core.models import Events
from django.contrib.auth.models import User


class Inscricao(models.Model):
    inscricao_id = models.AutoField(primary_key=True)
    usuario_inscrito = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, default=None)
    inscricao_confirmada = models.BooleanField(default=False)
    inscricao_atualizada = models.BooleanField(default=False, editable=False)

    class Meta:
        verbose_name_plural = "Inscrições"

    def __str__(self):
        return self.bootcamp.titulo_evento

    def checa_vaga(curso):
        if (curso.inscritos_confirmados <= curso.maximo_inscritos):
            Events.atualiza_curso(curso)
            return True
        else:
            return False

    def inscreve(curso_selecionado, usuario):
        nova = Inscricao(usuario_inscrito=usuario,curso=curso_selecionado)
        nova.save()
