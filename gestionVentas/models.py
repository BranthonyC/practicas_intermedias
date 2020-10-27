from django.db import models

from producto.models import Producto
from cliente.models import Cliente
# Create your models here.

TIPO_VENTA = (
    ('LOCAL','LOCAL'), 
    ('DOMICILIO', 'DOMICILIO'), 
) 

## creacion tabla ventas
class Venta(models.Model):
    no_orden = models.CharField(max_length=50)
    cliente = models.ForeignKey("cliente.Cliente",on_delete=models.SET_NULL, null=True)
    vendedor = models.CharField(max_length=20)
    fecha_facturacion = models.DateField()
    fecha_entrega = models.DateField(blank=True,null=True)
    tipo_venta=models.CharField(choices=TIPO_VENTA,max_length=20)
    #lista_productos = models.ForeignKey("ListaProductos",on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("Venta")
        verbose_name_plural = ("Ventas")

    def __str__(self):
        return self.no_orden

## lista de productos por orden de venta
class ListaProductos(models.Model):

    #producto = models.models.ForeignKey("Producto", verbose_name=_(""), on_delete=models.CASCADE)    
    no_orden = models.CharField(max_length=50)
    producto = models.ForeignKey("producto.Producto",on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    subtotal = models.FloatField()

    #categoria=models.ForeignKey('Categoria',on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = ("ListaProducto")
        verbose_name_plural = ("ListaProductos")


    #def get_absolute_url(self):
     #   return reverse("_detail", kwargs={"pk": self.pk})