#       Valores
#Até 100 km: R$ 10,00
#Entre 100 km e 200 km: R$ 20,00
#Acima de 200 km: R$ 30,00

try:
    distancia = float(input("Digite a distância percorrida(km): "))
    print(f"A distancia a ser percorrida é: {distancia:.1f}km")

    if distancia <= 100:
        print("Valor do pedágio é R$10,00")
    elif 101 <= distancia <= 200:
        print("Valor do pedágio é R$20,00")
    elif distancia >= 6000:
        print("Ta indo pra onde amigao?")
    else:
        print("O valor do pedágio é R$30,00")

except ValueError:
    print("Insira um valor válido!")