def calculoPoupanca():
    try:
        quant_paes = int(input("Digite a quantidade de paes: "))
        quant_broas = int(input("Digite a quantidade de broas: "))

        total = (quant_paes * 0.12) + (quant_broas * 1.5)
        valor_poupanca = total * 0.9

        print("O total arrecardado com a vendas de pães e broas foram: %.2f " %total)
        print("Valor para poupança: %.2f" %valor_poupanca)
    except:
        print("Degite somente números")
        calculoPoupanca()
        

calculoPoupanca()
