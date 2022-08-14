'''
11 - Desenha moldura. Construa uma função que desenhe um retângulo com um símbolo dentro de
cada quadrado. Essa função deve receber dois parâmetros, linhas e colunas.
'''
import os

def retangulo(linhas, colunas, simbolo):
    y = (f"|_{simbolo}_|")   
    for i in range(0,linhas):
        print(colunas * y)

try:
    print("*----------Formando retângulo----------*\n\n")
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
    simbolo = str(input("Digite o símbolo desejado: "))
    os.system("cls")
    retangulo(linhas, colunas, simbolo)
except ValueError:
    os.system("cls")
    print("Você digitou algo errado. Tente novamente!\n")