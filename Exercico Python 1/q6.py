def calculoAneis():
    quant = int(input("Quantidade de frangos: "))

    chip_identificacao = (quant * 4)
    chip_alimentacao = (quant * 2 * 3.5)
    
    print("Valor total do chip de identificação: %.2f" %(chip_identificacao))
    print("Valor total do chip de alimentacao: %.2f" %(chip_alimentacao))
    print("Somatorio: %.2f" %(chip_identificacao + chip_alimentacao))

calculoAneis()
