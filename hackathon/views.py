from django.shortcuts import render
from .models import Hackathon

def hackathon(request):
    hackathon_artigo = Hackathon.objects.all()

    context = {
        'hackathon_artigo': hackathon_artigo,
    }
    return render(request, 'hackathon.html', context)
