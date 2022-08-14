'''
Crie um programa em que o usário poderá digitar n notas e, ao fim, deverá retornar a média aritmética dessas notas.
'''


import os

print("*----------Calculador de N médias!----------*\n\n")
try:
  nome = str(input("Digite o nome do aluno(a): "))
  materia = str(input("Digite a matéria: "))
  os.system("cls")
  print("Agora vamos as notas:\n\n")
  count = 1
  lista = []
  for i in range(100):
    n1 = float(input(f"Digite a nota {count}: "))
    lista.append(n1)
    count += 1
    escolha = str(input("Adicionar mais uma nota? S/N  "))
    if(escolha == 's' or escolha == 'S'):
      os.system("cls")
      continue
    elif(escolha == 'n' or escolha == 'N'):
      break
    else:
      os.system("cls")
      print("Comando inválido! Tente novamente.\n\n")
  os.system("cls")
  print(f"Você adicionou {count} notas: {lista}\n")
  media = round(sum(lista)/len(lista),2)
  print(f"Fazendo a média aritmética, temos o resultado: {media}")
except ValueError:
  os.system("cls")
  print("Você digitou algo errado! Tente novamente.")
print("\n-------------------------------\n")