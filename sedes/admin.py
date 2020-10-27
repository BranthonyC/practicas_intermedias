from django.contrib import admin
from .models import *

# Register your models here.
class SedeAdmin(admin.ModelAdmin):
        model = Sede
        list_display = ['alias','direccion','municipio','encargado']

admin.site.register(Sede,SedeAdmin)
admin.site.register(Departamento)
admin.site.register(Municipio)