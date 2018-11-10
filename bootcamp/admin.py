from django.contrib import admin
from .models import *

class BootcampAdmin(admin.ModelAdmin):
    list_display = ['titulo_evento', 'data_inicial_evento', 'data_final_evento', 'inscritos_totais', 'inscritos_confirmados','maximo_inscritos', 'ativo']

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['bootcamp', 'em_exibicao']

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Bootcamp, BootcampAdmin)
admin.site.register(Professor)
