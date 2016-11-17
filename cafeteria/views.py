from django.shortcuts import render
from .models import Categoria

def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'cafeteria/inicio.html', {'categorias': categorias})
