from django.shortcuts import render

# Create your views here.

#uma view Django é uma função Python 
def index(request):
    return render(request, 'index.html')

def comunidade(request):
    return render(request, 'comunidade.html')

def noticias(request):
    return render(request, 'noticias.html')

def oque(request):
    return render(request, 'oque.html')

def personagem(request):
    return render(request, 'personagem.html')

def produtos(request):
    return render(request, 'produtos.html')

