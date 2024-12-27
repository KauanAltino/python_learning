venda_bananas = int(input("Quantidade vendida de bananas: "))
venda_macas = int(input("Quantidade vendida de maçãs: "))

if venda_bananas > venda_macas:
    print("As bananas venderam mais que as maçãs")
elif venda_bananas == venda_macas:
    print("Ocorreu um empate! A quantidade vendida foi a mesma")
else:
    print("As maçãs venderam mais que as bananas")
