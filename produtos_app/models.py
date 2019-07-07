from django.db import models
from django.contrib.auth import get_user_model
class Produto(models.Model):
    codigo = models.CharField(max_length=20, db_index=True)
    nome = models.CharField(max_length=100, blank=False)
    descricao = models.TextField(max_length=200, blank=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

