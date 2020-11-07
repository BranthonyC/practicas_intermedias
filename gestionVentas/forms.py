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
TIPO_REP= [
    ('mes', 'mes'),
    ('dia', 'dia'),
    ('semana', 'semana'),
    ('vendedor_mes', 'vendedor - mes'),
    ('vendedor_semana', 'vendedor - semana'),
    
    ]
MES= [
    ('NO', '---'),
    ('enero', 'enero'),
    ('febrero', 'febrero'),
    ('marzo', 'marzo'),
    ('abril', 'abril'),
    ('mayo', 'mayo'),
    ('junio', 'junio'),
    ('julio', 'julio'),
    ('agosto', 'agosto'),
    ('septiembre', 'septiembre'),
    ('octubre', 'octubre'),
    ('noviembre', 'noviembre'),
    ('diciembre', 'diciembre'),
    
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
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    tipo_venta = forms.CharField(label='Tipo de descuento', widget=forms.Select(choices=TIPO_DESCUENTO))

class Seleccionar_orden2Form(forms.Form):   
    #no_orden=forms.ModelChoiceField(queryset=Venta.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    desc2 = forms.CharField(label='Ordenes', widget=forms.Select(choices=DETALLE))

class Reportes_Form(forms.Form):   
    #no_orden=forms.ModelChoiceField(queryset=Venta.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    anio = forms.IntegerField()
    mes = forms.IntegerField(required=False)
    semana= forms.IntegerField(required=False)
    tipo_rep = forms.CharField(label='Tipo-reporte:', widget=forms.Select(choices=TIPO_REP))
    #semana1= forms.IntegerField()

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

class TerminarVentaForm(forms.Form):
    aceptador=forms.CharField(max_length=25)