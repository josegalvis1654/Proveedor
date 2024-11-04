from django.db import models


class Proveedores(models.Model):
    nit = models.CharField(max_length=10)
    razon_social = models.CharField(max_length=20)
    representante_legal= models.CharField(max_length=20)
    direcion = models.CharField(max_length=10)
    telefono = models.IntegerField()
    vehiculo_asociado = models.CharField(max_length=20)
