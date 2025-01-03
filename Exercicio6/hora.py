#Horario de entrada entre 8h e as 18h.

try:
    hora = int(input("Digite a hora atual (24h - Sem os minutos): "))

    if 0 <= hora < 8 or hora > 18:
        print("Acesso negado!")
    elif 8 <= hora <= 18:
        print("Acesso liberado!")
    else:
        print("Acesso negado!")  

except ValueError:
    print("Insira um valor de hora válido!")
