def q6():
    quant_dia = int(input("Quantidade de cigaros fumados por dia:"))
    anos = int(input("Quantos anos você ja fumou?"))

    tempoTotal = (((anos * 365) * quant_dia) /6)/ 24

    print("Tempo de vida perdido sera %.2f" %tempoTotal)


def q7():
    metros = int(input("Tamanho em metros quadrados da area a ser pintada:"))

    litros = 18
    calculoTinta = metros/3
    count = 1
    while(calculoTinta > litros):
        litros += 18
        count+=1

    print("Quantidade latas: %d, valor total: %.2f" %(count, count*80))

def q8():
    valor = int(input("Digite o valor = "))
    i=1
    total = 0
    valores = []
            
    while total < valor:
        total = i *(i+1) * (i+2)
        valores = [i, i+1, i+2]
        i+=1

    if(total == valor):
        print ("É triangular")
    else:
        print ("Não é triangular")

def q9(valor, lista):
    count = 0
    for i in lista:
        if i == valor:
            count +=1

    print("Quantidade de ocorrencias: %d" %count)

def q10():
    opostos = {"Alto": "Baixo",
               "Pequeno": "Grande",
               "Direita" : "Esquerda",
               "Certo" : "Errado",
               "Verdadeiro" : "Falso"}
    
    chave = input("Digite a chave de busca: ")

    while (chave != 'sair'):
        if(chave in opostos != False):
            print("O Oposto de %s é %s" %(chave,opostos[chave]))
        else:
            resposta = int(input("Oposto não encontrado, deseja adicionar? (1-Sim, 2- Não)"))
            if(resposta == 1):
                novo_oposto = input("Digite o nome do oposto de "+ chave + ":")
                opostos[chave] = novo_oposto

        chave = input("Digite a chave de busca: ")
        
q10()
