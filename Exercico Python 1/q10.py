def calculoDividas(salario, divida1, divida2):
    divida1 += divida1 *0.02
    divida2 += divida2 * 0.02

    sobra = salario - divida1 - divida2

    print("Restará R$ %.2f " %sobra)
    
calculoDividas(1200, 200, 120)
    
    
