from django.db import models
from tinymce.models import HTMLField
from core.models import Events

class Hackathon(Events):
    hackathon_id = models.AutoField(primary_key=True)
    proposta_hackathon = HTMLField()
    equipe = HTMLField()

    class Meta:
        verbose_name_plural = "Hackathon"

    def __str__(self):
        return self.titulo_evento
