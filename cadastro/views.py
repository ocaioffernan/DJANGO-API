from .serializers import UserSerializer, LoteSerializer, ProdutoSerializer, FornecedorSerializer, ClienteSerializer, ItemVendaSerializer, EstoqueMovimentacaoSerializer, VendaSerializer
from .models import Lote, Produto, Fornecedor, Cliente, ItemVenda, EstoqueMovimentacao, Venda, CategoriaProduto, Promocao, HistoricoPreco, ConfiguracaoPDV, LogAuditoria
from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class UserListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny] 

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny] 
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

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



# class CategoriaProdutoListCreate(generics.ListCreateAPIView):
#     queryset = CategoriaProduto.objects.all()
#     serializer_class = CategoriaProdutoSerializer

# class CategoriaProdutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CategoriaProduto.objects.all()
#     serializer_class = CategoriaProdutoSerializer


# class PromocaoListCreate(generics.ListCreateAPIView):
#     queryset = Promocao.objects.all()
#     serializer_class = PromocaoSerializer

# class PromocaoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Promocao.objects.all()
#     serializer_class = PromocaoSerializer


# class HistoricoPrecoListCreate(generics.ListCreateAPIView):
#     queryset = HistoricoPreco.objects.all()
#     serializer_class = HistoricoPrecoSerializer

# class HistoricoPrecoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HistoricoPreco.objects.all()
#     serializer_class = HistoricoPrecoSerializer


# class ConfiguracaoPDVListCreate(generics.ListCreateAPIView):
#     queryset = ConfiguracaoPDV.objects.all()
#     serializer_class = ConfiguracaoPDVSerializer

# class ConfiguracaoPDVRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ConfiguracaoPDV.objects.all()
#     serializer_class = ConfiguracaoPDVSerializer


# class LogAuditoriaListCreate(generics.ListCreateAPIView):
#     queryset = LogAuditoria.objects.all()
#     serializer_class = LogAuditoriaSerializer

# class LogAuditoriaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = LogAuditoria.objects.all()
#     serializer_class = LogAuditoriaSerializer

def rotas(request):
    return render(request, 'index.html')