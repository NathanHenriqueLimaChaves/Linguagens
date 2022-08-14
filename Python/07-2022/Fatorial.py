'''
Crie um programa que fará o fatorial de um número inteiro a ser recebido.
'''
import os

try:
  num = int(input("Digite apenas o número o qual você deseja o fatorial: "))
  os.system("cls")
  count = 0
  lista = []
  mult = 1
  if(num >= 0):
    for x in range(num):
       if(num == count):
        break
       fatorial = (num-count)
       lista.append(fatorial)
       count += 1
    for i in lista:
      mult *= i 
    print(f"Você escolheu fazer o fatorial do número: {num}\nFatorial => {lista} = {mult}")
  else:
    print("Número inválido. Tente novamente!")
except ValueError:
  print("Você digitou algo errado. Tente novamente!")
print("\n-------------------------------\n")