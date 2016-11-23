from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Categoria(models.Model):
    categoria = models.CharField(max_length=25)
    foto = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.categoria

class Producto(models.Model):
    producto = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='photos/')
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __Uncode__(self):
        return self.producto
    
    def get_absolute_url(self):
        return reverse('producto-list')
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.TextField()
    telefono = models.CharField(max_length=12)
    correo = models.CharField(max_length=25, default='N/A')
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.nombre
    
@receiver(post_delete, sender=Producto)
def producto_delete(sender, instance, **kwargs):
    instance.producto.delete(False)