from django.shortcuts import render
from .models import *

def Code_dojo(request):
    artigo_codedojo = Artigo_codedojo.objects.all().filter(em_exibicao=True)
    context = {
        'artigo_codedojo': artigo_codedojo
    }
    return render(request, 'codedojo.html', context)

def Codedojo_pagina(request,codedojo_id):
    try:
        artigo_codedojo_page = Artigo_codedojo.objects.get(pk=codedojo_id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    return render(request, 'codedojoartigo.html', {'artigo_codedojo_page': artigo_codedojo_page})
