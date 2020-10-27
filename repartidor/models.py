from django.db import models

# Create your models here.
class Repartidor(models.Model):
    dpi = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    nacimiento = models.DateField()
    correo = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.dpi