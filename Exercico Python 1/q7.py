def calculoLitros():
    quant360l = int(input("Quantidade de garrafas de 360ml: "))
    quant600l = int(input("Quantidade de garrafas de 600ml: "))
    quant2l = int(input("Quantidade de garrafas de 2L: "))

    total = ((quant360l * 360)/ 1000 + (quant600l * 600)/ 1000) + quant2l

    
    print("A quantidade total de litros é: %.2f" %total)

calculoLitros()
