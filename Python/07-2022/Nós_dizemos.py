'''
Crie um programa que receberá n números e retornará as seguintes informações:
 -O maior número fornecido
 -O menor número fornecido
 -A soma de todos os números fornecidos
 -A multiplicação de todos os números fornecidos
'''


import os

print("*----------Bem-vindo(a) ao Nós dizemos!----------*\n")
numeros = []
mult = 1
try:
  num = int(input("Digite um número inteiro: "))
  numeros.append(num)
  while True:
    num = int(input("Digite outro número inteiro: "))
    numeros.append(num)
    escolha = str(input("Deseja adicionar mais um número? S/N  "))
    os.system("cls")
    if(escolha == 'N' or escolha == 'n'):
      break
    elif(escolha == 'S' or escolha == 's'):
      continue
    else:
      print("Comando inválido. Tente novamente!\n\n")
  os.system("cls")
  for i in numeros:
    mult *= i
  print(f"Baseado nos números que você nos forneceu, podemos afirmar o seguinte:\n\n")
  print(f"[1]O maior número que você nos forneceu foi o número {max(numeros)}")
  print(f"[2]O menor número que você nos forneceu foi o número {min(numeros)}")
  print(f"[3]A soma de todos os números que você nos forneceu é igual a {sum(numeros)}")
  print(f"[4]Multiplicando todos os números que você nos forneceu resulta em {mult}")
except ValueError:
  print("Você digitou algo errado. Tente novamente!")
print("\n-------------------------------\n")