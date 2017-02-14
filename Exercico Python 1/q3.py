def valorConta():
    valor_total = float(input("Valor da Conta: "))

    divisao = int(valor_total / 3) 
    resto = valor_total % 3
    valorCarlos = divisao + resto 
 
    print("Carlos paga %.2f, André paga %.2f, Felipe paga %.2f  " %(divisao, divisao, valorCarlos))     

valorConta()
