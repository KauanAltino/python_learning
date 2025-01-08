# dados
# A renda mensal precisa ser maior que R$ 2.000,00.
# A parcela não pode ultrapassar 30% da renda.

try:
    print("Guia de empréstimo")
    print("Renda tem que ser maior 2mil reais")
    print("Parcela tem que ser menor que 30% da sua renda")
    renda = float(input("Digite o valor da sua renda mensal(R$): "))
    parcela = float(input("Digite o valor da parcela desejada: "))
    valorParcela = 0.3 * renda


    if renda < 2000.00:
        print("Empréstimo Reprovado: renda abaixo de 2mil reais")
    elif parcela > valorParcela:
        print("Empréstimo Reprovado: parcela acima de 30% da renda")
    else:
        print("Empréstimo Aprovado!")


except ValueError:
    print("ERROR")
    print("Insira um valor válido")