from rest_framework import serializers
from .models import Produto, Fornecedor, Cliente, Lote, ItemVenda, EstoqueMovimentacao



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
        fields = '__all__'

class EstoqueMovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueMovimentacao
        fields = '__all__'
