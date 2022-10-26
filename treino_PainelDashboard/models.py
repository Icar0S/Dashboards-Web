from django.db import models
import datetime

class Produto(models.Model):
  nome = models.CharField(max_length=150)

  def __str__(self) -> str:
    return self.nome

class Vendedor(models.Model):
  nome = models.CharField(max_length=50)

  def __str__(self) -> str:
    return self.nome

class Vendas(models.Model):
  nome_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
  vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
  total = models.FloatField()
  data = models.DateField(default=datetime.datetime.now())

  def __str__(self) -> str:
    return self.nome_produto.nome
