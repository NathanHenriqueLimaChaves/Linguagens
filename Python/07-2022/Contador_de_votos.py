'''
Crie um programa que irá receber n votos dos eleitores e retornar quantos votos cada candidato teve e as porcentagens de cada um.
'''
import os

print("*----------Urna!----------*\n\n")
try:
  count = 1
  lista = []
  candidato_a = 0
  candidato_b = 0
  candidato_c = 0
  n = int(input("Quantos eleitores irão votar: "))
  os.system("cls")
  for i in range(1,n+1):
    os.system("cls")
    print("[10]Candidato A  [20]Candidato B  [30]Candidato C\n")
    voto = int(input("Qual o número do seu candidato? "))
    if(voto == 10):
      candidato_a += 1
      os.system("cls")
      print("Voto contabilizado! Obrigado :)")
      os.system("pause")
    elif(voto == 20):
      candidato_b += 1
      os.system("cls")
      print("Voto contabilizado! Obrigado :)")
      os.system("pause")
    elif(voto == 30):
      candidato_c += 1
      os.system("cls")
      print("Voto contabilizado! Obrigado :)")
      os.system("pause")
    else:
      os.system("cls")
      print("Nenhum candidato com esse número. Tente novamente!")
  total_a = round((candidato_a/n)*100,2)
  total_b = round((candidato_b/n)*100,2)
  total_c = round((candidato_c/n)*100,2)
  os.system("cls")
  print(f"Dos {n} eleitores, {candidato_a} votaram no Candidato A. Porcentagem => {total_a}%")
  print(f"Dos {n} eleitores, {candidato_b} votaram no Candidato B. Porcentagem => {total_b}%")
  print(f"Dos {n} eleitores, {candidato_c} votaram no Candidato C. Porcentagem => {total_c}%")
  print("\n\n")
except ValueError:
  os.system("cls")
  print("Você digitou algo errado! Tente novamente.")
print("\n-------------------------------\n")