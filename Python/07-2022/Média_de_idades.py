'''
O programa deverá receber n idades e ao fim mostrar fatos sobre as idades inseridas. 
'''
import os

print("*----------Média de idades!----------*\n\n")
try:
  count = 1
  lista = []
  n = 100
  for i in range(1,n):
    idade = int(input(f"Digite a idade da pessoa {count}: "))
    if(idade <= 0 or idade > 150):
      print("Idade fora do intervalo possível.")
      break
    else:
      lista.append(idade)
      escolha = str(input("Adicionar mais idades? S/N  "))
      if(escolha == 's' or escolha == 'S'):
        count += 1
        n += 1
        os.system("cls")
        continue
      elif(escolha == 'n' or escolha == 'N'):
        break
      else:
        os.system("cls")
        print("Comando inválido! Tente novamente.\n\n")
  os.system("cls")
  media = round(sum(lista)/len(lista),2)
  if(media > 0 and media <= 25):
    print(f"Alguns fatos:\n[1]Você digitou as idades de {count} pessoas!\n[2]A média das idades é igual a {media} anos!\n[3]Baseado na média da idade, o grupo é um grupo jovem!")
  elif(media > 25 and media <= 60):
    print(f"Alguns fatos:\n[1]Você digitou as idades de {count} pessoas!\n[2]A média das idades é igual a {media} anos!\n[3]Baseado na média da idade, o grupo é um grupo adulto!")
  elif(media > 60):
    print(f"Alguns fatos:\n[1]Você digitou as idades de {count} pessoas!\n[2]A média das idades é igual a {media} anos!\n[3]Baseado na média da idade, o grupo é um grupo idoso!")
except ValueError:
  os.system("cls")
  print("Você digitou algo errado! Tente novamente.")
print("\n-------------------------------\n")