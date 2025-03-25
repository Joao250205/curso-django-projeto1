from django.shortcuts import render
#HTTP request e o servidor retorna para ele uma HTTP response

def home(request):
    return render(request, 'recipes/home.html',status=201,context={
        'nome': 'joão',
    })


# Create your views here.
