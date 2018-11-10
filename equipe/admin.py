from django.contrib import admin
from .models import Integrante_equipe, CodeRed_descricao

class Integrante_equipeAdmin(admin.ModelAdmin):
    list_display = ['integrante_nome', 'ativo']

admin.site.register(Integrante_equipe, Integrante_equipeAdmin )
admin.site.register(CodeRed_descricao)
