from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sucesso_pagamento(request):
    return render(request, 'sucesso.html')

@csrf_exempt
def falha_pagamento(request):
    return render(request, 'falha.html')
