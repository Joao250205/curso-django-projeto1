from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#HTTP request e o servidor retorna para ele uma HTTP response

def home(request):
    return render(request, 'recipes/home.html',status=201,context={
        'nome': 'joão',
    })


def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')

# Create your views here.
