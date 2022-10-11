from django.db import models
from lojas.models import Loja

# Create your models here.
class Colecao(models.Model):
    loja = models.ForeignKey(Loja, on_delete= models.CASCADE, primary_key=True)

    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome