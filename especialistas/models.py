from django.db import models

class Especialista(models.Model):
    nome = models.CharField (max_length=100)
    especialidade = models.CharField (max_length=150)
    endereco = models.CharField(max_length=150)
    cr = models.CharField(max_length=20)
    telefone = models.CharField (max_length = 50)
    descricao = models.CharField (max_length = 200)

