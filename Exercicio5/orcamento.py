# LIMITE R$3.000,00

try:
    despesa = float(input("Digite o valor das despesas do mês(R$): "))

    if despesa <= 1999.99:
        print("Você está dentro do orçamento")
    elif 2000 <= despesa <= 2999.99:
        print("Alerta! Está chegando ao limite do orçamento")
    else:
        print("Alerta! Você Ultrapassou o orçamento!")

except ValueError:
    print("Insira um valor válido")
