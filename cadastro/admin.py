from django.contrib import admin
from .models import Fornecedor, Produto, Cliente, Venda, ItemVenda, EstoqueMovimentacao, Lote

admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(ItemVenda)
admin.site.register(EstoqueMovimentacao)
admin.site.register(Lote)
