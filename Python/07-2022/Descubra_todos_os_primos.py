import os

print("*----------Descubra todos os primos!----------*\n\n")
try:
  num = int(input("Digite o número de parada desejado: "))
  os.system("cls")
  if(num > 1):
    count = 0
    lista = []
    count_geral = 0
    for i in range(1,num+1):
      if(i % i == 0 and i % 2 != 0 and i % 3 != 0):
        count += 1
        lista.append(i)
    print(f"Foram realizadas {count} divisões entre o número 1 e o número fornecido, {num}.\nResultado:{len(lista)} números primos nesse intervalo!\nSão eles: {lista}\n\n")
    os.system("pause")
  else:
    print("Número inválido. Tente novamente!")
except ValueError:
  print("Você digitou algo errado! Tente novamente.")