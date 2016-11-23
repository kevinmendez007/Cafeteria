from .models import Categoria, Producto
from django.shortcuts import render, get_object_or_404
from .forms import CategoriaForm
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

def primera_vista(request):
    return HttpResponse('Esta es mi primera vista')

def base(request):
    return render(request, 'cafeteria/base.html')

def categoria(request):
    categoria_lista = Categoria.objects.all()
    context = {'object_list': categoria_lista}
    return render(request, 'cafeteria/categoria.html', context)

def categoria_detalle(request, pk):
    categoria = Categoria.objects.get(id=pk)
    context = {'object': categoria}
    return render(request, 'cafeteria/categoria_detail.html', context)

class ProductoListView(ListView):
    model = Producto
    
class ProductoDetailView(DetailView):
    model = Producto
    
class CategoriaListView(ListView):
    model = Categoria
    
class CategoriaDetailView(DetailView):
    model = Categoria
    
class ProductoUpdate(UpdateView):
    model = Producto
    
class ProductoCreate(CreateView):
    model = Producto

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-lista')
    




    
    
    
    
def categoria_producto(request, pk):
    categoria = Categoria.objects.get(id=pk)
    return render(request, 'cafeteria/categoria_producto.html', {'cat': categoria})

def agregar_categoria(request):
    if request.method == "POST":
        formulario = CategoriaForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            categoria = formulario.save()
            categoria.save()
            return HttpResponseRedirect('/')
    else:
        formulario = CategoriaForm()
    return render(request, 'cafeteria/categoria_edit.html', {'formulario': formulario})

def editar_categoria(request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        if request.method == "POST":
            form = CategoriaForm(request.POST, instance=categoria)
            if form.is_valid():
                categoria = form.save()
                post.save()
                #return redirect('blog.views.post_detail', pk=post.pk)
                return HttpResponseRedirect('/')
        else:
            form = CategoriaForm(instance=post)
        return render(request, 'categoria/categoria_edit.html', {'form': form})