from django.db import models

# Create your models here.


class Tipo(models.Model):
    nombre = models.CharField


    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField
    precio = models.IntegerField
    stock = models.TextField
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
