from django import forms
from django.forms import ModelForm
from .models import Venta,ListaProductos

#from .models import Producto,Historial_Cambios,Categoria,DetalleCategorias,SolicitudTransferenciaProductos,DetalleTransferencias
from producto.models import Producto
from cliente.models import Cliente
import datetime
from .models import Venta,ListaProductos


TIPO_VENTA= [
    ('LOCAL', 'LOCAL'),
    ('DOMICILIO', 'DOMICILIO'),
  
    ]


TIPO_DESCUENTO= [
    ('CON_DESCUENTO', 'CON DESCUENTO'),
    ('SIN_DESCUENTO', 'SIN DESCUENTO'),
  
    ]

DESCUENTO= [
    ('SIN_DESCUENTO', 'SIN_DESCUENTO'),
    ('CINCO', 'APLICAR 5%'),
    ('DIEZ', 'APLICAR 10%'),
    ('QUINCE', 'APLICAR 15%'),
  
    ]
DETALLE= [
    ('A', '-----'),
    
    ]
### SOLO EL USUARIO VENDEDOR PUEDE CREAR UNA NUEVA VENTAS
class Crear_ventaForm(forms.Form):  
    #no_orden= forms.IntegerField() 
    cliente=forms.ModelChoiceField(queryset=Cliente.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    fecha_facturacion = forms.DateField(initial=datetime.date.today, required=False)
    fecha_entrega = forms.DateField(initial=datetime.date.today, required=False)
    tipo_venta = forms.CharField(label='Tipo de venta', widget=forms.Select(choices=TIPO_VENTA))

   
class ListaProductosForm(forms.Form):   
    
    #no_orden=forms.ModelChoiceField(queryset=Venta.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    producto=forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    cantidad= forms.IntegerField()
    porcentaje = forms.CharField(label='Aplicar descuentooo', widget=forms.Select(choices=DESCUENTO))
    
class Seleccionar_ordenForm(forms.Form):   
    no_orden=forms.ModelChoiceField(queryset=Venta.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    desc = forms.CharField(label='Aplicar descuento', widget=forms.Select(choices=DESCUENTO))

class Seleccionar_DetalleForm(forms.Form):   
    no_orden=forms.ModelChoiceField(queryset=Venta.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    tipo_venta = forms.CharField(label='Tipo de descuento', widget=forms.Select(choices=TIPO_DESCUENTO))

class Seleccionar_orden2Form(forms.Form):   
    #no_orden=forms.ModelChoiceField(queryset=Venta.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    desc2 = forms.CharField(label='Ordenes', widget=forms.Select(choices=DETALLE))

class NuevaListaForm(forms.ModelForm):
    class Meta:
        model = ListaProductos
        fields = [
            'no_orden',
            'producto',
            'cantidad'
        ]

class NuevaVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
        'no_orden',
        'cliente',
        'vendedor',
        'fecha_facturacion',
        'fecha_entrega',
        'tipo_venta'

        ]
