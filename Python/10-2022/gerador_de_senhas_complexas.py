import os
import random
from random import shuffle

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while True:
    print("__________Gerador de Senhas PyPassword__________\n\n")
    print("Bem-vindo(a) ao gerador de senhas PyPassword!")
    print("Responda a três simples perguntas e receba uma senha!")
    os.system("pause")
    os.system("cls")
    while True:
        try:
            nr_letras = int(
                input("Quantas letras você quer que sua senha tenha?\n"))
            nr_simbolos = int(
                input(f"Quantos símbolos você quer que sua senha tenha?\n"))
            nr_numeros = int(
                input(f"E quantos números você quer em sua senha?\n"))
            os.system("cls")

            senha = []
            for letra in range(0, nr_letras):
                rand = random.choice(letras)
                senha.append(rand)

            for simbolo in range(0, nr_simbolos):
                rand = random.choice(simbolos)
                senha.append(rand)

            for numero in range(0, nr_numeros):
                rand = random.choice(numeros)
                senha.append(rand)

            # print(senha)
            shuffle(senha)
            # print(senha)

            senha_final = (''.join(senha))
            print(f"Aqui está a sua nova senha: {senha_final}")
            os.system("pause")
            os.system("cls")
            break
        except ValueError:
            os.system("cls")
            print("Você digitou algo errado. Tente novamente!\n\n")
