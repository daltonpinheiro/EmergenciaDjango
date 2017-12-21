from django.shortcuts import render,redirect
from .models import Paciente
from .forms import FormPaciente

def mostra(request):
	return(render(request,"teste.html",{}))

# Create your views here.

def RegistraPaciente(request):
    if request.method == "POST":
        form = FormPaciente(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author =  request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('formulario')
    else:
        form = FormPaciente()
    return render(request, 'Banco de dados CR.html', {'form': form})
