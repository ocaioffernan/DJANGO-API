from rest_framework import serializers
from .models import Produto, Fornecedor, Cliente, Lote, ItemVenda, EstoqueMovimentacao, Venda,  CategoriaProduto, Promocao, HistoricoPreco, ConfiguracaoPDV, LogAuditoria
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active']  # Inclua 'is_active' se necessário

    def create(self, validated_data):
        # Cria o usuário com hash na senha
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # Atualiza o usuário, tratando a senha corretamente
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

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


class CategoriaProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProduto
        fields = '__all__'

class PromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocao
        fields = '__all__'

class HistoricoPrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoPreco
        fields = '__all__'

class ConfiguracaoPDVSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracaoPDV
        fields = '__all__'

class LogAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAuditoria
        fields = '__all__'