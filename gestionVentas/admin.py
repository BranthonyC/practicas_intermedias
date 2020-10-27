from django.contrib import admin

from .models import Venta,ListaProductos
# Register your models here.
## SOLO EL VENDEDOR PUEDE CREAR VENTAS
class gestionVentasAdmin(admin.ModelAdmin):
        model = Venta
        list_display = ['no_orden','cliente','vendedor','fecha_facturacion','fecha_entrega','tipo_venta']
        search_fields = ['no_orden']
        list_filter=['fecha_facturacion','fecha_entrega']

class ListaAdmin(admin.ModelAdmin):
        model = ListaProductos
        list_display = ['no_orden','producto','cantidad','precio','subtotal']
        search_fields = ['no_orden']
        list_filter=['no_orden',]

admin.site.register(Venta,gestionVentasAdmin)
admin.site.register(ListaProductos,ListaAdmin)
