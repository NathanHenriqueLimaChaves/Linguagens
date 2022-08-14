'''
6 - Faça uma função que informe a quantidade de dígitos de um determinado número inteiro in-
formado.
'''
import os
lista = []
while True:
    try:
        print("*----------Contador de dígitos----------*\n\n")
        print("OBS - Digite 0 para sair do programa!\n")
        numero = int(input("Digite um número inteiro: "))
        if(numero == 0):
            os.system("cls")
            print("Volte sempre! :)")
            break
        else:
            def digitos(numero):
                numero = str(numero)
                for i in numero:
                    lista.append(i)
                tamanho = int(len(lista))
                print(f"O número tem um total de {tamanho} dígitos.")
            digitos(numero)
            lista.clear()
            os.system("pause")
            os.system("cls")
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente!\n")