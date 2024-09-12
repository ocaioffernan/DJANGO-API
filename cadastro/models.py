from django.db import models
from django.core.exceptions import ValidationError

class Fornecedor(models.Model):
    razaoSocial = models.CharField(max_length=100)
    nomeFantasia = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=18, unique=True)  # CharField para permitir pontuações
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

    def save(self, *args, **kwargs):
        if not self.pk:
            nome_normal = self.nome.lower() 
            if Produto.objects.filter(nome__iexact=nome_normal).exclude(pk=self.pk).exists():
                raise ValidationError('Produto já existe')

        if self.estoque_minimo > self.estoque_maximo:
            raise ValidationError('O valor mínimo não pode ser maior que o Estoque máximo')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - R${self.precoVenda}"

class Lote(models.Model):
    lote_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='lotes')
    lote_numero = models.CharField(max_length=100, unique=True)
    data_fabricacao = models.DateField()
    data_validade = models.DateField()
    quantidade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lote {self.lote_numero} - {self.lote_produto.nome}"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11, unique=True)
    CEP = models.CharField(max_length=9)  # CharField para CEP formatado
    telefone = models.CharField(max_length=15, blank=True)  # CharField para telefones formatados
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    PAGAMENTO_CHOICES = [
        ('pix', 'Pix'),
        ('dinheiro', 'Dinheiro'),
        ('cartão de crédito', 'Cartão de Crédito'),
        ('cartão de débito', 'Cartão de Débito')
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    data_venda = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    metodo_pagamento = models.CharField(max_length=50, choices=PAGAMENTO_CHOICES)
    
    def __str__(self):
        return f"Venda {self.id} - Total: {self.total}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2) # omitir no serializer
    
    def save(self, *args, **kwargs):
        if self.produto.estoque_atual <= self.produto.estoque_minimo:
            raise ValidationError("Estoque insuficiente")

        self.subtotal = (self.produto.precoVenda * self.quantidade) - self.desconto
        super().save(*args, **kwargs)
        # Atualiza o total da venda
        self.venda.total = sum(item.subtotal for item in self.venda.itens.all())
        self.venda.save()
        self.produto.estoque_atual -= self.quantidade
        self.produto.save()
        
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
