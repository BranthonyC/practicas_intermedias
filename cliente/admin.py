from django.contrib import admin

from .models import Cliente

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
        model = Cliente
        list_display = ['nombre','nit','dpi','direccion']

admin.site.register(Cliente,ClienteAdmin)