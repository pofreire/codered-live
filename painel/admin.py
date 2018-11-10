import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib import admin
from bootcamp.models import Bootcamp
from django.contrib import messages
from .models import Inscricao
from django.http import HttpResponse

def Atualiza_inscricao(modeladmin, request, queryset):
    for Inscricao in queryset:
        if Inscricao.inscricao_confirmada == True:
            if Inscricao.inscricao_atualizada == False:
                Inscricao.inscricao_atualizada = True
                bootcamp.confirma_inscricao(Inscricao.bootcamp)
                Atualiza_inscricao.short_description = 'Atualiza a inscricao'
                messages.success(request, 'Você atualizou essa inscriao')
                Inscricao.save()
            else:
                messages.error(request, 'Voce ja atualizou essa inscrição')
        else:
                messages.error(request, 'O Usuário precisa estar com a inscrição confirmada')




def Gera_relatorio_pdf(modeladmin, request, queryset):
    for Inscricao in queryset:
        if Inscricao.inscricao_confirmada == True:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
            # ['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' -  para abrir opção de baixar o pdf

            carga_horaria = ("%s Horas totais" % (Inscricao.bootcamp.carga_horaria_bootcamp))
            data = ("Do dia %s ao dia %s" % (Inscricao.bootcamp.data_inicial_bootcamp, Inscricao.bootcamp.data_final_bootcamp))

            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            p.drawCentredString(300, 790, Inscricao.bootcamp.titulo_bootcamp)
            p.line(30,780,580,780)
            p.drawString(30,765,carga_horaria)
            p.drawString(370,765,data)
            p.line(30,760,580,760)
            # End writing


            p.showPage()
            p.save()

            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)

            return response
        else:
            messages.error(request, 'Participante com inscrição nao confirmada')

class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['bootcamp','usuario_inscrito', 'inscricao_confirmada']
    actions = [Atualiza_inscricao, Gera_relatorio_pdf ]
admin.site.register(Inscricao, InscricaoAdmin)
