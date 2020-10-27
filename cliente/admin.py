from django.contrib import admin

from .models import Cliente

# Register your models here.
## SOLO EL VENDEDOR PUEDE CREAR CLIENTES

class ClienteAdmin(admin.ModelAdmin):
        model = Cliente
        list_display = ['nombre','nit','dpi','direccion']

admin.site.register(Cliente,ClienteAdmin)