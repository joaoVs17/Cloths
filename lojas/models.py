from django.db import models
from user.models import User
from django.utils import timezone

# Create your models here.

class Plano(models.Model):
    nome = models.CharField(max_length=6)
    preco = models.FloatField()

    def __str__(self):
        return self.nome

class Loja(models.Model):

    loja_admin = models.ForeignKey(User, on_delete=models.CASCADE)

    nome_loja = models.CharField(max_length=50)
    email_loja = models.EmailField(max_length=255, null=True)
    telefone_loja = models.CharField(max_length=16, null=True)
    cnpj = models.CharField(max_length=18)

    cep_loja = models.CharField(max_length=9)
    estado_loja = models.CharField(max_length=100)
    cidade_loja = models.CharField(max_length=100)
    rua_loja = models.CharField(max_length=100)
    bairro_loja = models.CharField(max_length=100)

    numero_cartao = models.CharField(max_length=64)
    nome_cartao = models.CharField(max_length=64)
    cvv = models.CharField(max_length=64)
    data_expiracao = models.DateTimeField(64)

    date_joined_loja = models.DateTimeField(default=timezone.now)

    logo_loja = models.ImageField(upload_to='logos_lojas/',null=True)

    plano = models.ForeignKey(Plano, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.nome_loja