try:
    print("Insira valores inteiros apenas.")
    valorA = int(input("Digite os dias para a Atividade A: "))
    valorB = int(input("Digite os dias para a Atividade B: "))
    valorC = int(input("Digite os dias para a Atividade C: "))
    if valorA > 0 and valorB > 0 and valorC > 0:
        valorTotal = valorA + valorB + valorC
        print("A estimativa de dias é: " + str(valorTotal))
    else:
        print("ERROR: Há valores negativos.")
except ValueError:
    print("Erro: Você deve inserir apenas números inteiros.")
