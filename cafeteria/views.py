from django.shortcuts import render
from .models import Categoria
from django.shortcuts import render, get_object_or_404

def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'cafeteria/inicio.html', {'categorias': categorias})

def categoria_producto(request, pk):
    pro = get_object_or_404(Categoria, pk=pk)
    return render(request, 'cafeteria/categoria_producto.html')
    