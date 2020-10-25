from django import forms
from django.forms import ModelForm
from .models import Producto,Historial_Cambios,Categoria,DetalleCategorias


class Historial_Cambios_FORM(forms.Form):   
    producto=forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    cantidad_nueva=forms.IntegerField(widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Cantidad',
                                    }))
    motivo=forms.CharField(max_length=150,
                                    widget=forms.Textarea(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Motivo de actualizacion',
                                    }))
    
                            
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'sku',
            'codigo_barras',
            'nombre',
            'descripcion',
            'precio',
            'cantidad',
            'sku',
        ]
        labels = {
            'cantidad': 'Cantidad en inventario',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form_control', 'cols': 25, 'rows': 8}),
        } 

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre_categoria',
        ]

class DetalleCategoriasForm(forms.ModelForm):
    class Meta:
        model = DetalleCategorias
        fields = [
            'producto',
            'categoria'
        ]
