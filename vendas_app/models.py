from django.db import models
from clientes_app .models import Cliente
from produtos_app .models import Produto
from django.contrib.auth import get_user_model

class NotaFiscal(models.Model):
    numero = models.IntegerField(db_index=True)
    data_venda = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, related_name='notas_fiscais', on_delete=models.CASCADE)
    item = models.ForeignKey(Produto, related_name='vendas', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

