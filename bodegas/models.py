from django.db import models
from users.models import CustomUser


tipo_estado = (
    ('ACTIVA','ACTIVA'), 
    ('INACTIVA', 'INACTIVA'), 
) 

class Bodega(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    estado=models.CharField(choices=tipo_estado,max_length=10)
    creador = models.ForeignKey(CustomUser, related_name="creador_bodegas", on_delete=models.CASCADE, blank=True, null=True)
    encargado = models.ForeignKey(CustomUser, related_name="encargados_bodegas", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("winery_detail", kwargs={"pk": self.pk})