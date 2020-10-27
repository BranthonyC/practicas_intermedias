from django.db import models
from users.models import CustomUser

# Create your models here.
class Sede(models.Model):
    alias = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    departamento = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    encargado = models.ForeignKey(CustomUser, related_name="encargados", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
    
    def __str__(self):
        return self.alias
    
    def get_absolute_url(self):
        return reverse("campus_detail", kwargs={"pk": self.pk})