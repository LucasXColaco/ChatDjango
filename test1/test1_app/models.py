from django.db import models

# Create your models here.

class ChatTable(models.Model):
    time_stamp = models.TimeField(auto_now=True)
    usuario = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=300)

    def __str__(self):
        return (f'{self.usuario}: {self.mensagem}')