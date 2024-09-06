from django.db import models

class Fornecedor(models.Model):
    razaoSocial = models.CharField(max_length=100)
    nomeFantasia = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=18)  # CharField para permitir pontuações
    CEP = models.CharField(max_length=9)  # CharField para CEP formatado
    telefone = models.CharField(max_length=15, blank=True)  # CharField para telefones formatados
    email = models.EmailField(unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomeFantasia

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.FileField(blank=True, null=True)
    estoque_atual = models.IntegerField()
    estoque_minimo = models.IntegerField(default=0)
    estoque_maximo = models.IntegerField(default=0)
    precoCompra = models.DecimalField(max_digits=10, decimal_places=2)
    precoVenda = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Lote(models.Model):
    
    lote_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='lotes')
    lote_numero = models.CharField(max_length=100, unique=True)
    data_fabricacao = models.DateField()
    data_validade = models.DateField()
    quantidade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lote {self.lote_numero} - {self.lote_produto.nome}"

    class Meta:
        ordering = ['data_validade']
        verbose_name_plural = "Lotes"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11, unique=True)
    CEP = models.CharField(max_length=9)  # CharField para CEP formatado
    telefone = models.CharField(max_length=15, blank=True)  # CharField para telefones formatados
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    data_venda = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Venda {self.id} - Total: {self.total}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.produto.nome} - Venda {self.venda.id}"
    
class EstoqueMovimentacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('ajuste', 'Ajuste'),
    ]
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    motivo = models.CharField(max_length=255, blank=True, null=True)
    data_movimentacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movimentação {self.tipo} - Produto {self.produto.nome}"
