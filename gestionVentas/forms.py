from django import forms
from django.forms import ModelForm
from .models import Venta,ListaProductos
## SOLO EL VENDEDOR PUEDE CREAR VENTAS
#from .models import Producto,Historial_Cambios,Categoria,DetalleCategorias,SolicitudTransferenciaProductos,DetalleTransferencias
from producto.models import Producto
from cliente.models import Cliente
import datetime
from .models import Venta,ListaProductos


TIPO_VENTA= [
    ('LOCAL', 'LOCAL'),
    ('DOMICILIO', 'DOMICILIO'),
  
    ]
class Crear_ventasForm(forms.Form):  
    no_orden= forms.IntegerField() 
    cliente=forms.ModelChoiceField(queryset=Cliente.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    fecha_facturacion = forms.DateField(initial=datetime.date.today, required=False)
    fecha_entrega = forms.DateField(initial=datetime.date.today, required=False)
    tipo_venta = forms.CharField(label='Tipo de venta', widget=forms.Select(choices=TIPO_VENTA))

   
class ListaProductosForm(forms.Form):   
    
    no_orden=forms.ModelChoiceField(queryset=Venta.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    #producto2=forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    producto=forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    cantidad= forms.IntegerField()
    
  

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
