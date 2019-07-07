from  django.db import models
from django .contrib .auth import get_user_model


class Cliente(models.Model):
    email = models.EmailField(max_length=50, db_index=True)
    nome = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome