'''
7 - Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721
'''
import os
lista = []
while True:
    try:
        print("*----------Inversor----------*\n\n")
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
                lista.reverse()
                array = lista
                resultado = [''.join(array)]
                print(f"{numero} -> {resultado[0]}")
            digitos(numero)
            lista.clear()
            os.system("pause")
            os.system("cls")                
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente!\n")