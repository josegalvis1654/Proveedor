from django.db import models

class Proveedores(models.Model):
    nit = models.CharField(max_length=10)
    razon_social = models.CharField(max_length=200)
    representante_legal= models.CharField(max_length=200)
    direcion = models.CharField(max_length=100)
    telefono = models.PositiveBigIntegerField()
    vehiculo_asociado = models.CharField(max_length=200)