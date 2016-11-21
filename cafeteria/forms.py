from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        modelo = Categoria
        campos = ('nombre', 'foto',)