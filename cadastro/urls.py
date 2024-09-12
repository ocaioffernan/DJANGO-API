from django.urls import path
from .views import LoteListCreate, LoteRetrieveUpdateDestroy, ProdutoListCreate, FornecedorListCreate, ItemVendaListCreate, EstoqueMovimentacaoListCreate,\
     ClienteListCreate, ProdutoRetrieveUpdateDestroy, FornecedorRetrieveUpdateDestroy, ClienteRetrieveUpdateDestroy, ItemVendaRetrieveUpdateDestroy, EstoqueMovimentacaoRetrieveUpdateDestroy, LoteRetrieveUpdateDestroy, \
    VendaListCreate, VendaRetrieveUpdateDestroy, rotas


urlpatterns = [
    path('lotes/', LoteListCreate.as_view(), name='lote-list-create'),
    path('lote/<int:pk>', LoteRetrieveUpdateDestroy.as_view(), name='lote-retrieve'),
    path('produtos/', ProdutoListCreate.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>', ProdutoRetrieveUpdateDestroy.as_view(), name='produtos-retrieve'),
    path('fornecedores/', FornecedorListCreate.as_view(), name='fornecedores-list-create'),
    path('fornecedores/<int:pk>', FornecedorRetrieveUpdateDestroy.as_view(), name='fornecedores-retrieve'),
    path('clientes/', ClienteListCreate.as_view(), name='clientes-list-create'),
    path('clientes/<int:pk>', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-retrieve'),
    path('itemvendas/', ItemVendaListCreate.as_view(), name='itemvenda-list-create'),
    path('itemvenda/<int:pk>', ItemVendaRetrieveUpdateDestroy.as_view(), name='itemvenda-retrieve'),
    path('estoque_mov/', EstoqueMovimentacaoListCreate.as_view(), name='estoquemovimentacao-list-create'),
    path('estoque_mov/<int:pk>', EstoqueMovimentacaoRetrieveUpdateDestroy.as_view(), name='estoquemovimentacao-retrieve'),
    path('vendas/', VendaListCreate.as_view(), name='vendas-list-create'),
    path('vendas/<int:pk>', VendaRetrieveUpdateDestroy.as_view(), name='cliente-retrieve'),
    path('', rotas, name='rotas')
]