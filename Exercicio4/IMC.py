#IMC = peso / (altura * 2)
#Abaixo do peso (IMC < 18.5)
#Peso normal (18.5 <= IMC < 25)
#Acima do peso (IMC >= 25)
#Obesidade grau 1: IMC entre 30,0 e 34,9
#Obesidade grau 2 (severa): IMC entre 35,0 e 39,9
#Obesidade grau 3 (mórbida): IMC ≥ 40,0
#Acima de 800kg "impossivel"

try:
    pesokg = float(input("Digite o seu peso(kg): "))
    altura = float(input("Digite a sua altura(m): "))
    imc = pesokg / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Você está no peso normal")
    elif 25 >= imc <= 29:
        print("Você está acima do peso")
    elif 30 >= imc <= 34.99:
        print("Você está com obesidade grau 1")
    elif 35 >= imc <= 39.99:
        print("Você está com obesidade grau 2")
    elif imc >= 40:
        print("Você está com obesidade grau 3")
    
except ValueError:
    print("Insira um valor válido")

