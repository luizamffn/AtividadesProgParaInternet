def vendaCamisa():
    try:
        quant_p = int(input("Quantidade de camisas P: "))
        quant_m = int(input("Quantidade de camisas M: "))
        quant_g = int(input("Quantidade de camisas G: "))

        total = (quant_p * 10) + (quant_m * 12) + (quant_g * 15)

        print("Valor Total: %.2f " %total)
    except:
        print("Degite somente números")
        vendaCamisa()
        

vendaCamisa()
