try:
    temp = float(input("Digite a temperatura atual: "))
    
    if temp > 100:
        print("Chama o bombeiro!")
    elif 70 < temp <= 100:
        print("Perigo!")
    elif temp > 25:
        print("Alerta! Temperatura excedeu o limite.")
    else:
        print("Temperatura estável")
except ValueError:
    print("Insira um valor de temperatura válido.")
