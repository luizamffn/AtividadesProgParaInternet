#2. Escreva	o	comando	necessários	para	criar	no	shell	do	Python:	
#a. Um	cliente;	
#b. Um	fornecedor;	
#c. Um	produto	
#d. Um	pedido;	
#e. Incluir	itens	em	um	pedido;	
#f. Uma	venda;	g. Incluir	itens	em	uma	venda.


cliente = Cliente(cpf ="055.002.044-34", nome ="Carla", endereco ="Rua das flores", 
	complemento = "ultima rua", cidade = "Teresina", estado = "PI", cep = "640000"
	foneResidencial = "2222-2222", foneTrabalho = "2222-22222", 
	redaFamiliar =2500, email = "carla@gmail.com")
cliente.save()

fornecedor = Fornecedor(cnpj = "0098487498-1000", nome = "FazBem", 
	endereco ="Rua Barroso", complemento = "prox a pintos", 
	cidade = "Teresina", estado = "PI", cep = "640000"
	fone = "2222-2222", responsavel = "Claudio", website = "fazbem.com.br")
fornecedor.save()

produto = Produto(nomeProduto = "cadeado", quantidade =10, minQuantidade =5)
produto.save()

pedido = Pedido(dataPedido = "2017-02-02", dataRecebimento ="2017-15-02", 
	precoTotal = 300, codFornecedor = fornecedor)
pedido.save()

itemPedido = ItemPedido(codPedido = pedido, codProduto = produto, precoUnitario =30, 
	quantidade =10)
itemPedido.save()

venda = Venda(dataVenda = "2017-02-03", valorTotal = 200, codCliente = cliente)
venda.save()

itemVenda = ItemVenda(codVenda = venda, codProduto = produto, precoUnitario =10, quantidade =20)
itemVenda.save()


#3. Escreva	o	comando	necessários	para	
#criar	no	shell	do	Python	que	retorne:	
#a. Todos	os	clientes;	
#b. Todas	as	vendas	de	um	cliente;	
#c. Um	pedido;	
#d. Todos	os	itens	de	um	pedido;	
#e. Produtos	que	atingiram	o	estoque	mínimo.	

Cliente.objects.all()
Venda.objects.filter(codCliente = 1)
Pedido.objects.get(id =3)
ItemPedido.objects.filter(codPedido = 3)






