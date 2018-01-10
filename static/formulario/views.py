from django.shortcuts import render,redirect
from .models import Paciente
from .forms import FormPaciente
from django.contrib.auth.decorators import login_required,permission_required

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


   
