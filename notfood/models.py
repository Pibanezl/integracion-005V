from django.db import models
from PIL import Image
# Create your models here.


class Tipo(models.Model):
    nombre = models.CharField(default='', max_length=40)


    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    foto = models.ImageField(null=True, upload_to='producto')
    precio = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
