def quantidadeSanduiche():
    quant = int(input("Quantidade de sanduiches: "))

    quant_queijo = (quant * 50)/1000
    quant_presunto = (quant * 50)/1000
    quant_carne = (quant * 100)/1000
 
    print("Para fazer esssa quantidade de sanduiche precisara de: ")
    print("%.3f quilos de queijo " %(quant_queijo))
    print("%.3f quilos de presunto " %(quant_presunto))
    print("%.3f quilos de carne " %(quant_carne))

quantidadeSanduiche()
