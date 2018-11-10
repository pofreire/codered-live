from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import *

def bootcamp(request):
    bootcamp_ativo = Artigo.objects.all().filter(em_exibicao=True)
    bootcamps = Artigo.objects.all().exclude(em_exibicao=True)
    context = {
        'bootcamp_ativo': bootcamp_ativo,
        'bootcamps' : bootcamps
    }
    return render(request, 'bootcamps.html', context)

def bootcamp_pagina(request,artigo_id):
    try:
        bootcamp_artigo = Artigo.objects.get(pk=artigo_id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    return render(request, 'botcampartigo.html', {'bootcamp_artigo': bootcamp_artigo})
