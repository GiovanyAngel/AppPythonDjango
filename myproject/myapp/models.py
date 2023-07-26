from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'myapp'
    
    def __str__(self):
        return self.nombre
    
class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    foto = models.ImageField(upload_to='prductos/', blank=True)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.nombre