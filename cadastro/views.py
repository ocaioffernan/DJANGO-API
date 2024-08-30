from .serializers import InscricaoSerializer, ProdutoSerializer, FornecedorSerializer, ClienteSerializer
from .models import Inscricao, Produto, Fornecedor, Cliente
from rest_framework import generics


class InscricaoListCreate(generics.ListCreateAPIView):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer


class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class FornecedorListCreate(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class ClienteListCreate(generics.ListCreateAPIView):
    queryset =  Cliente.objects.all()
    serializer_class = ClienteSerializer


class InscricaoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer


class ProdutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class FornecedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

