import os
numeros = []
count = 0
try:
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
    while count < 10:
        num = int(input("Digite outro número inteiro: "))
        numeros.append(num)
        count += 1
    os.system("cls")
    multiplicacao = 1
    for i in numeros:
        multiplicacao *= i
    print(f"Você digitou os seguintes números: {numeros}\nA multiplicação desses números é igual à: {multiplicacao}")
except ValueError:
    print("Você digitou algo errado. Tente novamente!")
