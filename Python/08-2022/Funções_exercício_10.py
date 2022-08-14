'''
10 - Embaralhar a palavra. Construa uma função que receba uma string como parâmetro e devol-
va outra string com os caracteres embaralhados. Por exemplo: se função receber a palavra 
"Python", pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma alea-
tória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou 
caixa baixa, independentemente de como foram digitados. 
'''
import os
from random import randint, sample
lista = []
lista_2 = []
def embaralhar(dado):
    for i in dado:
        lista.append(i)
    #print(lista)
    tamanho = int(len(lista))
    sorteados = sample(range(0, tamanho), tamanho)
    #print(sorteados)
    n = 0
    for i in lista:
        lista_2.append(lista[sorteados[0+n]])
        n += 1
    #print(lista_2)
    print("".join(lista_2))

try:
    print("*----------Embaralhar palavras----------*\n\n")
    dado = str(input("Digite uma palavra: "))
    os.system("cls")
    print(f"Você digitou {dado}\nEmbaralhamos e ficou assim:")
    dado = dado.lower()
    embaralhar(dado)
except ValueError:
    os.system("cls")
    print("Você digitou algo errado. Tente novamente!")