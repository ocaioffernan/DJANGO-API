from django.db import models


# Create your models here.
class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nascimento = models.IntegerField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    CEP = models.IntegerField()
    escolaridade = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
