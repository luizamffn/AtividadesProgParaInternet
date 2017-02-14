def calculoPoupanca2():
    quant01 = int(input("Quantidade de moedas de 0,01 centavos:"))
    quant05 = int(input("Quantidade de moedas de 0,05 centavos:"))
    quant10 = int(input("Quantidade de moedas de 0,10 centavos:"))
    quant25 = int(input("Quantidade de moedas de 0,25 centavos:"))
    quant50 = int(input("Quantidade de moedas de 0,50 centavos:"))
    quant1 = int(input("Quantidade de moedas de 1 real:"))

    valor_quebrados = ((quant01 * 0.01) + (quant05 * 0.05) + (quant10 * 0.1) + (quant25 * 0.25) + (quant50 * 0.5))
    valor_real = quant1 + valor_quebrados

    print("A quantidade economizada em reis é %.2f" %valor_real)

calculoPoupanca2()
    
    
