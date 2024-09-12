from rest_framework import serializers
from .models import Produto, Fornecedor, Cliente, Lote, ItemVenda, EstoqueMovimentacao, Venda



class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = ['quantidade', 'desconto', 'venda', 'produto', 'subtotal']
        read_only_fields = ['subtotal']

    def create(self, validated_data):
        item = super().create(validated_data)
        return item

class EstoqueMovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueMovimentacao
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ['metodo_pagamento', 'cliente', 'total']
        read_only_fields = ['total']