from django.shortcuts import render
from .models import Integrante_equipe, CodeRed_descricao

def Equipe(request):
    integrante = Integrante_equipe.objects.all().filter(ativo=True)
    descricao = CodeRed_descricao.objects.all()
    context = {
        'integrante': integrante,
        'descricao' : descricao,
    }
    return render(request, 'equipe.html', context)
