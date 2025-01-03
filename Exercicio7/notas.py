#Aprovado: Média >= 7
#Recuperação: 5 <= Média < 7
#Reprovado: Média < 5

#3 NOTAS DE ENTRADA
#CALCULAR MEDIA FINAL
#MOSTRAR RESULTADO FINAL

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media_final = (nota1 + nota2 + nota3) / 3
    print(f"Sua média final é: {media_final:.2f}")

    if media_final < 5:
        print("Reprovado!")
    elif 5 <= media_final < 7:
        print("Recuperação!")
    else:
        print("Aprovado!")

except ValueError:
    print("Insira um valor válido!")
