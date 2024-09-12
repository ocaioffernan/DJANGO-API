from .serializers import LoteSerializer, ProdutoSerializer, FornecedorSerializer, ClienteSerializer, ItemVendaSerializer, EstoqueMovimentacaoSerializer, VendaSerializer
from .models import Lote, Produto, Fornecedor, Cliente, ItemVenda, EstoqueMovimentacao, Venda
from rest_framework import generics
from django.shortcuts import render


class LoteListCreate(generics.ListCreateAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
class VendaListCreate(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    
class VendaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


class FornecedorListCreate(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class ClienteListCreate(generics.ListCreateAPIView):
    queryset =  Cliente.objects.all()
    serializer_class = ClienteSerializer

class ItemVendaListCreate(generics.ListCreateAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class EstoqueMovimentacaoListCreate(generics.ListCreateAPIView):
    queryset = EstoqueMovimentacao.objects.all()
    serializer_class = EstoqueMovimentacaoSerializer


class LoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


class ProdutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class FornecedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ItemVendaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class EstoqueMovimentacaoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstoqueMovimentacao.objects.all()
    serializer_class = EstoqueMovimentacaoSerializer

def rotas(request):
    return render(request, 'index.html')