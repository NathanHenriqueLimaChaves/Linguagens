import math
print("Bem vindo(a) ao cálculo de raízes do segundo grau!\n")
try:
    a = float(input("Digite o valor de 'a': "))
    if(a != 0):
        b = float(input("Digite o valor de 'b': "))
        c = float(input("Digite o valor de 'c': "))
        delta = (b**2)-(4*a*c)
        raiz_delta = math.sqrt(delta)
        if(delta != 0 and delta >= 1):
            print("O delta é maior que zero. Portanto, possui duas raízes reais e distintas.")           
            x = (-b+raiz_delta)/(2*a)
            x2 = (-b-raiz_delta)/(2*a)
            x_round = round(x, 3)
            x2_round = round(x2, 3)
            print(f"As raízes são: {x_round} e {x2_round}. ")
        elif(delta == 0):
            print("O delta da equação é igual a zero. Portanto, possui apenas uma raíz real!")
            x = (-b+raiz_delta)/(2*a)
            x_round = round(x, 3)
            print(f"A raíz da equação é {x_round}.")
        elif(delta < 0):
            print("A equação não possui raízes reais.")
    else:
        print("A equação não é do segundo grau!")
except ValueError:
    print("Você não digitou um número! Tente novamente.")
