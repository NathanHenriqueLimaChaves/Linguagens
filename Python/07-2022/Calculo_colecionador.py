'''
Faça um programa que pergunte a um colecionador quantos CDs ele tem e o preço de cada um dos CDs.
Ao final, mostre o valor total gasto por esse colecionador em sua coleção e o valor médio de cada CD.
'''

import os

print("*----------Colecionador!----------*\n\n")
try:
  count = 1
  lista = []
  cds = int(input("Digite a quantidade de Cds em sua coleção: "))
  os.system("cls")
  for i in range(1,cds+1):
    preco = float(input(f"Digite o preço do CD {count}: R$"))
    if(preco >= 0):
      os.system("cls")
      lista.append(preco)      
      print(f"O CD {count} custou R${preco} reais.")
      count += 1
      os.system("pause")
      os.system("cls")
    else:
      os.system("cls")
      print("Valor inválido! Tente novamente.\n\n")
  total = sum(lista)
  media = round(total/count,2)
  os.system("cls")
  print(f"O Sr(a). gastou um total de R${total} reais em sua coleção de {cds} CDs!\nPreço médio de R${media} reais por CD.")
except ValueError:
  os.system("cls")
  print("Você digitou algo errado! Tente novamente.")
print("\n-------------------------------\n")