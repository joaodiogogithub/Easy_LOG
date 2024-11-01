from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=16)
    address = models.CharField(max_length=100)

class Stock (models.Model):
    materia = models.CharField(max_length=100, null=False, blank=False)
    quanty = models.IntegerField(null=False, blank=False)

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null= False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quanty = models.IntegerField(null=False, blank=False)



