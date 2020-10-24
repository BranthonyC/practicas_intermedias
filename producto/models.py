from django.db import models

# Create your models here.

class Producto(models.Model):
    sku = models.CharField(max_length=150)
    codigo_barras = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150)
    categorias = models.CharField(max_length=150)
    precio = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    id = models.IntegerField()
    nombre_categoria=models.CharField(max_length=50)