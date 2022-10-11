from email.policy import default
from django.utils import timezone
from typing import Tuple
from unittest.util import _MAX_LENGTH
from django.db import models
from colecoes.models import Colecao

# Create your models here.

class TipoTamanho(models.Model):
    nome_tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_tipo

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255)
    tipo_tamanho = models.ForeignKey(TipoTamanho, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_categoria


class Roupa(models.Model):

    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    nome_roupa = models.CharField(max_length=255)
    preco = models.FloatField()

    pp = models.PositiveIntegerField(null=True, default=0)
    p = models.PositiveIntegerField(null=True, default=0)
    m = models.PositiveIntegerField(null=True, default=0)
    g = models.PositiveIntegerField(null=True , default=0)
    gg = models.PositiveIntegerField(null=True, default=0)
    xg = models.PositiveIntegerField(null=True, default=0)

    t1 = models.PositiveIntegerField(null=True, default=0)
    t2 = models.PositiveIntegerField(null=True, default=0)
    t3 = models.PositiveIntegerField(null=True, default=0)
    t4 = models.PositiveIntegerField(null=True, default=0)
    t5 = models.PositiveIntegerField(null=True, default=0)
    t6 = models.PositiveIntegerField(null=True, default=0)


    foto = models.ImageField(upload_to='fotos_roupas/', null=True)

    descricao = models.TextField(max_length=400, null=True)

    data_adicao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome_roupa+'/'+self.colecao.nome+'/'+self.colecao.loja.nome_loja+'/'+str(self.pk)
