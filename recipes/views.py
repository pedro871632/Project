from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):

    return render(request,"recipes/home.html",context = {
        "name":"Pedro Lucas"
    })
    

def sobre(request):
    return render(request, "temporary/index.html")

def contato(request):
    return HttpResponse("Estou em contatos !")