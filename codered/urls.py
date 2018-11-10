from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from register.views import Registrar, Login, Logout
from painel.views import Inscrever
from equipe.views import Equipe
from codedojo.views import Code_dojo, Codedojo_pagina
from home.views import home
from bootcamp.views import bootcamp,bootcamp_pagina
from hackathon.views import hackathon
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registrar/$', Registrar),
    url(r'^entrar/$', Login),
    url(r'^sair/$', Logout),
    url(r'^painel/$', Inscrever),
    url(r'^equipe/$', Equipe),
    url(r'^codedojo/$', Code_dojo),
    url(r'^codedojo/(?P<codedojo_id>\d+)$',Codedojo_pagina),
    url(r'^bootcamps/$', bootcamp),
    url(r'^bootcamps/(?P<artigo_id>\d+)$',bootcamp_pagina),
    url(r'^hackathon/$', hackathon),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^pagamento/', include('pagamento.urls', namespace='pagamento')),
    url(r'^$', home),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
