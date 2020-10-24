from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    dpi = models.CharField(max_length=13, default="3025958692359")
    nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=20)
    dpi = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.dpi

    def get_absolute_url(self):
        return reverse("cliente_detail", kwargs={"pk": self.pk})

