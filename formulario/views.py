'''Sistema desenvolvido por Dalton funcionário da EBSERH(HUMAP)'''
from django.shortcuts import render,redirect
from .models import Paciente
from .forms import FormPaciente
from django.contrib.auth.decorators import login_required,permission_required
import time

def mostra(request):
	return(render(request,"teste.html",{}))

# Create your views here.
@login_required
def RegistraPaciente(request):
    if request.method == "POST":
        form = FormPaciente(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author =  request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('RegistraPaciente')
    else:
        form = FormPaciente()
    return render(request, 'Banco de dados CR.html', {'form': form})


   
def grafico(request):
    tab=Paciente.objects.raw('select id,prioridade,count(*)as qt from formulario_paciente group by prioridade')
    tab2=Paciente.objects.raw("select id,strftime('%Y%m', Data)as AnoMes ,sum(case prioridade    when 'AMARELO' then 1    else  0 end) as amarelo, \
        sum(case prioridade    when 'AZUL' then 1    else  0 end) as azul,sum(case prioridade    when 'BRANCO' then 1    else  0 end) as branco, \
        sum(case prioridade  when 'LARANJA' then 1   else  0 end) as laranja,sum(case prioridade    when 'VERDE' then 1    else  0 end) as verde, \
        sum(case prioridade  when 'VERMELHO' then 1    else  0 end) as vermelho, \
        count(*)as qtde \
        from formulario_paciente group by 2")
    context = {
        'dia':time.strftime('dia %d-%m-%Y às %H:%M'),
        'valor': tab,
        'valor2':tab2
    }
    return render(request,'graficos_plotly.html',context)