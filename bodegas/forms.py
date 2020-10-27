from django import forms
from django.forms import ModelForm
from .models import Bodega


class bodega_forms(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = [
            'nombre',
            'direccion',
            'estado',
            'encargado'
        ]