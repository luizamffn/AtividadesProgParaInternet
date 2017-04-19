def q3(n1, n2):
    if n1 > n2:
        return "%d é o maior " %n1 
    elif n2 > n1:
        return "%d é o maior " %n2
    else:
        return "%d é igual a %d" %(n1,n2)

def q4(n1, n2,n3):
    troca = 1

    while(troca > 0):
        troca = 0
        if n1 > n2:
            n1,n2 = n2,n1
            troca += 1
        if n2 > n3:
            n2,n3 = n3,n2
            troca += 1

    return "%d,%d,%d" %(n1,n2,n3)

def q5(n1):
    if n1%2 ==0:
        return "verdadeiro"
    else:
        return "Falso"

def q6(valor):
    if(valor > 20):
        return "Vá ao cinema"
    else:
        return "Fique vendo TV"

def q7(nome, sexo):
    if sexo == "M":
        return "Ilma Sr. %s" %nome
    elif sexo == "F":
        return "Ilma Sra. %s" %nome

def q8(num):
    if num >= 1:
        return "Positivo"
    elif num == 0:
        return "Igual a zero"
    else:
        return "Negativo"

def q9(num):
    if num%5 ==0:
        return "verdadeiro"
    else:
        return "Falso"
    
def q10(distancia, tempo):
    return distancia/tempo

def q11(temperatura):
    if(temperatura > 36.5):
        return "Está com febre"
    else:
        return "Está sem febre"

def q12(num):
    if num%7 ==0:
        return "O número é multiplo de 7"
    else:
        return "O número não é multiplo de 7"

def q13(num):
    if num%3 ==0:
        return "verdadeiro"
    else:
        return "Falso"

def q14(ano):
    idade = 2017 - ano
    if(idade >= 18):
        return "Poderá votar nessas eleiçoes"
    else:
        return "Não poderá votar nessas eleiçoes"

def q15(letra):
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        return "Verdadeiro"
    else:
        return "Falso"
