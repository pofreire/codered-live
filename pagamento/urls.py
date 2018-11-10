from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sucesso/$', views.sucesso_pagamento, name='sucesso'),
    url(r'^falha/$', views.falha_pagamento, name='falha'),
]
