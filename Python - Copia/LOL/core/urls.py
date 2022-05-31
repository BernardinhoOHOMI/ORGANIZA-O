from django.urls import path
from .views import *

urlpatterns = [
    path('index.html', index),
    path('comunidade.html', comunidade),
    path('noticias.html', noticias),
    path('oque.html', oque),
    path('personagem.html', personagem),
    path('produtos.html', produtos)
]
