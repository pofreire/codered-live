from django.contrib import admin
from .models import *

class HackathonAdmin(admin.ModelAdmin):
    list_display = ['titulo_evento', 'inscritos_totais', 'inscritos_confirmados','maximo_inscritos', 'ativo']

admin.site.register(Hackathon, HackathonAdmin)
