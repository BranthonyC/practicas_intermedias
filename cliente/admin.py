from django.contrib import admin

from .models import Cliente

# Register your models here.

# SOLO EL ROL VENDEDOR PUEDE AGREGAR NUEVOS CLIENTESs
class ClienteAdmin(admin.ModelAdmin):
        model = Cliente
        list_display = ['nombre','nit','dpi','direccion']

admin.site.register(Cliente,ClienteAdmin)