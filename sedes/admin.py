from django.contrib import admin
from .models import Sede

# Register your models here.
class SedeAdmin(admin.ModelAdmin):
        model = Sede
        list_display = ['alias','direccion','departamento','municipio','encargado']

admin.site.register(Sede,SedeAdmin)