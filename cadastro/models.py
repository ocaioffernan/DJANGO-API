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

class Fornecedor(models.Model):
    razaoSocial = models.CharField(max_length=100)
    nomeFantasia = models.CharField(max_length=100)
    CNPJ = models.IntegerField()
    CEP = models.IntegerField()
    telefone = models.IntegerField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nomeFantasia

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.FileField()
    quantidade = models.IntegerField()
    precoCompra = models.IntegerField()
    precoVenda = models.IntegerField()
    forcenedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11)
    CEP = models.IntegerField()
    telefone = models.IntegerField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
