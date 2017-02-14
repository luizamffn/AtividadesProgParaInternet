def calculoSalario():
    horas_normal = int(input("Quantidade de horas normais trabalhadas: "))
    horas_extra = int(input("Quantidade de horas extra trabalhadas: "))

    valor_bruto = (horas_normal * 10) + (horas_extra *15)
    valor_liquido = valor_bruto * 0.9
    
    print("Salário bruto: %.2f" %(valor_bruto))
    print("Salário liquido: %.2f" %(valor_liquido))

calculoSalario()
