try:
    numero = int(input("Digite um número: "))
    if(numero == 1):
        print("Domingo!!!")
    elif(numero == 2):
        print("Segunda!!!")
    elif(numero == 3):
        print("Terça!!!")
    elif(numero == 4):
        print("Quarta!!!")
    elif(numero == 5):
        print("Quinta!!!")
    elif(numero == 6):
        print("Sexta!!!")
    elif(numero == 7):
        print("Sabado!!!")
    else:
        print("Número inválido") 
except ValueError:
    print("Você digitou algo errado. Tente novamente!")