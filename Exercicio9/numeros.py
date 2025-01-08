try:
    numero = int(input("Insira um numero inteiro: "))

    if numero % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é ímpar")



except ValueError:
    print("ERROR")
    print("Insira um valor válido e inteiro")