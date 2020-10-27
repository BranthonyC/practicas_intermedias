from django.db import models
from users.models import CustomUser

# Create your models here.
class Bodega(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    estado = models.CharField(max_length=30)
    encargado = models.ForeignKey(CustomUser, related_name="encargados_bodegas", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("winery_detail", kwargs={"pk": self.pk})