# classe para exercico

from django.db import models


class Cliente (models.Model):
	cpf = models.CharField(max_length = 14)
	nome = models.CharField(max_length = 30)
	endereco = models.CharField(max_length = 35)
	complemento = models.CharField(max_length = 50)
	cidade = models.CharField(max_length = 25)
	estado = models.CharField(max_length = 2)
	cep = models.CharField(max_length = 8)
	foneResidencial = models.CharField(max_length = 15)
	foneTrabalho = models.CharField(max_length = 15)
	rendaFamiliar = models.DecimalField(max_digits = 10, decimal_places = 2)
	email = models.CharField(max_length = 50)


	def __str_(self):
		return "%s - %s" %(self.nome, self.cpf)


class Venda (models.Model):
	dataVenda = models.DateTimeField()
	valorTotal = models.DecimalField(max_digits = 10, decimal_places = 2)
	codCliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

class Produto (models.Model):
	nomeProduto = models.CharField(max_length = 38)
	quantidade = models.IntegerField()
	minQuantidade = models.DecimalField(max_digits = 10, decimal_places = 2)


class ItemVenda (models.Model):
	codVenda = models.ForeignKey(Venda, on_delete = models.CASCADE)
	codProduto = models.ForeignKey(Produto, on_delete = models.CASCADE)
	precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)
	quantidade = models.IntegerField()


class Fornecedor (models.Model):
	cnpj = models.CharField(max_length = 14)
	nome = models.CharField(max_length = 38)
	endereco = models.CharField(max_length = 35)
	complemento = models.CharField(max_length = 50)
	cidade = models.CharField(max_length = 25)
	estado = models.CharField(max_length = 2)
	cep = models.CharField(max_length = 14)
	fone = models.CharField(max_length = 15)
	responsavel = models.CharField(max_length = 15)
	website = models.CharField(max_length = 80)


class Pedido (models.Model):
	dataPedido = models.DateTimeField()
	dataRecebimento = models.DateTimeField()
	precoTotal = models.DecimalField(max_digits = 10, decimal_places = 2)
	codFornecedor = models.ForeignKey(Fornecedor, on_delete = models.CASCADE)

	def __str__(self):
		return "%s - %s" %(self.id, self.precoTotal)

class ItemPedido (models.Model):
	codPedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
	codProduto = models.ForeignKey(Produto, on_delete = models.CASCADE)
	precoUnitario = models.DecimalField(max_digits = 10, decimal_places= 2)
	quantidade = models.IntegerField()








