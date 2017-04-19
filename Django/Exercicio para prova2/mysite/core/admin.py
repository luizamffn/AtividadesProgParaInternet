from django.contrib import admin
from .models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cpf','email', 'cidade')

admin.site.register(Cliente, ClienteAdmin)

class VendaAdmin(admin.ModelAdmin):
	list_display = ('dataVenda', 'valorTotal')

admin.site.register(Venda, VendaAdmin)


class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nomeProduto', 'quantidade','minQuantidade')

admin.site.register(Produto, ProdutoAdmin)

class FornecedorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cnpj','cidade', 'website')

admin.site.register(Fornecedor, FornecedorAdmin)


class PedidoAdmin(admin.ModelAdmin):
	list_display = ('dataPedido', 'dataRecebimento','precoTotal')

admin.site.register(Pedido, PedidoAdmin)

class ItemVendaAdmin(admin.ModelAdmin):
	list_display = ('codVenda','codProduto','precoUnitario')

admin.site.register(ItemVenda, ItemVendaAdmin)

class ItemPedidoAdmin(admin.ModelAdmin):
	list_display = ('codPedido','codProduto','precoUnitario', 'quantidade')

admin.site.register(ItemPedido, ItemPedidoAdmin)
