from ast import Delete
from django.db import models
from lojas.models import Loja
from user.models import User
from colecoes.models import Colecao
from roupas.models import Roupa

from django.utils import timezone
# Create your models here.

class Pedido(models.Model):

    usuario_pedinte = models.ForeignKey(User, on_delete=models.CASCADE)

    roupa_pedida = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    loja_para = models.ForeignKey(Loja, on_delete = models.CASCADE)
    colecao_de = models.ForeignKey(Colecao, on_delete=models.CASCADE)

    data_pedido = models.DateField(default=timezone.now)

    def __str__(self):
        return self.usuario_pedinte.nome +'/'+ self.loja_para.nome_loja+'/'+self.data_pedido
