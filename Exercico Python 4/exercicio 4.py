def q1():
    for i in range(100):
        print (i+1)

def q2():
    for i in range(100,0,-1):
        print (i)
        
def q3():
    count=0
    i = 0
    while (i <=100):
        if(count % 2 == 0):
            print (count)
            i+=1
        count+=1

def q4():
    for i in range(0,500,5):
        print (i)

def q5():
    for i in range(1,20):
        print (i**2)

#11. Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de
#3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de
#natalidade de 2% ano ano. Calcular e imprimir o tempo necessário
#para que a população do país A ultrapasse a população do país B. 

def q11(populacaoA,populacaoB, taxaA, taxaB):
    ano = 0
    while(populacaoA <= populacaoB):
        populacaoA += populacaoA * 0.03
        populacaoB += populacaoB *0.02
        ano+=1
    return ano
        
print(q11(5000000, 7000000, 3,2))
    
