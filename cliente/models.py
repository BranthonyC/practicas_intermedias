from django.db import models

# Create your models here.
## SOLO EL VENDEDOR PUEDE CREAR CLIENTES
class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=20)
    dpi = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.nombre