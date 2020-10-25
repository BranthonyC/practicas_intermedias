from django.contrib import admin
from producto.models import Producto,Categoria,DetalleCategorias,Historial_Cambios,SolicitudTransferenciaProductos,DetalleTransferencias
# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(DetalleCategorias)
admin.site.register(Historial_Cambios)
admin.site.register(SolicitudTransferenciaProductos)
admin.site.register(DetalleTransferencias)