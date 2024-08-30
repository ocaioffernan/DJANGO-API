from django.urls import path
from .views import InscricaoListCreate, InscricaoRetrieveUpdateDestroy, ProdutoListCreate, FornecedorListCreate,\
    ClienteListCreate, ProdutoRetrieveUpdateDestroy, FornecedorRetrieveUpdateDestroy, ClienteRetrieveUpdateDestroy


urlpatterns = [
    path('inscricoes/', InscricaoListCreate.as_view(), name='inscricao-list-create'),
    path('inscricoes/<int:pk>', InscricaoRetrieveUpdateDestroy.as_view(), name='inscricao-retrieve'),
    path('produtos/', ProdutoListCreate.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>', ProdutoRetrieveUpdateDestroy.as_view(), name='produtos-retrieve'),
    path('fornecedores/', FornecedorListCreate.as_view(), name='fornecedor-list-create'),
    path('fornecedores/<int:pk>', FornecedorRetrieveUpdateDestroy.as_view(), name='fornecedores-retrieve'),
    path('clientes/', ClienteListCreate.as_view(), name='clientes-list-create'),
    path('clientes/<int:pk>', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-retrieve'),
]