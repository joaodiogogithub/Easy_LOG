from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=16)
    endereco = models.CharField(max_length=100)

class Pedidos(models.Model):
    data = models.DateTimeField(null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)

class Estoque (models.Model):
    materia_prima = models.CharField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null= False, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(null=False, blank=False)



