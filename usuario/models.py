from django.db import models
from django.contrib.auth.models import User

class Usuario (User):
    CPF = models.CharField(max_length=11, unique=True, default='-', primary_key=True)
    datanascimento = models.IntegerField()
    cidade = models.CharField (max_length = 50)
    estado = models.CharField (max_length = 30)
    identificacao = models.CharField (max_length = 50)
    def __str__(self):
        return self.CPF
