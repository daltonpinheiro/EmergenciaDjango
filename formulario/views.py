from django.shortcuts import render,redirect

def mostra(request):
	return(render(request,"Banco de dados CR.html",{}))

# Create your views here.
