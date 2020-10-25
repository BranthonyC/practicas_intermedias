from django.db import models

# Create your models here.

class Producto(models.Model):
    sku = models.CharField(max_length=150)
    codigo_barras = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150)
    categorias = models.CharField(max_length=150)
    precio = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50)
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre_categoria

class DetalleCategorias(models.Model):
    producto = models.ForeignKey('Producto',on_delete=models.SET_NULL, null=True)
    categoria=models.ForeignKey('Categoria',on_delete=models.SET_NULL, null=True)

class Historial_Cambios(models.Model):
    producto=models.ForeignKey('Producto',on_delete=models.SET_NULL, null=True)
    cantidad_antigua=models.IntegerField()
    cantidad_nueva=models.IntegerField()
    motivo=models.CharField(max_length=150)
    bodeguero=models.CharField(max_length=50)
    fecha=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Historial_Cambio"
        verbose_name_plural = "Historial_Cambios"