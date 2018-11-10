from django.contrib import admin
from .models import *

class Artigo_codedojoAdmin(admin.ModelAdmin):
    list_display = ['code_dojo', 'em_exibicao']

class Code_dojo_Admin(admin.ModelAdmin):
    list_display = ['titulo_evento', 'data_inicial_evento', 'data_final_evento', 'inscritos_totais', 'inscritos_confirmados', 'maximo_inscritos', 'ativo' ]

admin.site.register(Artigo_codedojo, Artigo_codedojoAdmin )
admin.site.register(Code_dojo, Code_dojo_Admin)
