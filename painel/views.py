from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from bootcamp.models import Bootcamp
from .models import Inscricao
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm

@login_required(login_url='/entrar/')
def Inscrever(request):
    host = request.get_host()
    bootcamps = Bootcamp.objects.all().filter(ativo=True)
    paypal_dict = {
        "business": "otaviocha@gmail.com",
        "amount": "10.00",
        "item_name": "teste",
        "currency_code": "BRL",
        "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
        "return": 'http://{}{}'.format(host, reverse('pagamento:sucesso')),
        "cancel_return": 'http://{}{}'.format(host, reverse('pagamento:falha')),
        # "invoice": "unique-invoice-id",
        # https://django-paypal.readthedocs.io/en/stable/
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    if bootcamps.exists():
        if request.method == 'POST':
            bootcamp_selecionado = Bootcamp.objects.get(pk=request.POST['bootcamp_id'])
            if Inscricao.objects.filter(usuario_inscrito=request.user, bootcamp=bootcamp_selecionado):
                messages.success(request, 'Você ja esta inscrito nesse curso')
            else:
                if Inscricao.checa_vaga(bootcamp_selecionado) == True:
                    Inscricao.inscreve(bootcamp_selecionado, request.user)
                    messages.success(request, 'Inscrição realizada com sucesso')
                else:
                    messages.success(request, 'Infelizmente todas as vagas foram preenchidas')

    else:
        pass
    context = {
        'bootcamps' : bootcamps,
        'form' : form,
    }
    return render(request, 'painel.html', context)
