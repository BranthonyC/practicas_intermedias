from django.db import models
from users.models import CustomUser

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})


class Municipio(models.Model):
    nombre = models.CharField(max_length=150)
    departamento = models.ForeignKey(Departamento, related_name="departamento_padre", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("municipality_detail", kwargs={"pk": self.pk})


class Sede(models.Model):
    alias = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    #departamento = models.ForeignKey(Departamento, related_name="encargado_depto", on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, related_name="encargado_mun", on_delete=models.CASCADE, blank=True, null=True)
    encargado = models.ForeignKey(CustomUser, related_name="encargados", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
    
    def __str__(self):
        return self.alias
    
    def get_absolute_url(self):
        return reverse("campus_detail", kwargs={"pk": self.pk})
        