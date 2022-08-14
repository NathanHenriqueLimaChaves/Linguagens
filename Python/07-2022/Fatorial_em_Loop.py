
import os

while True:
  try:
    num = int(input("Entre 0 e 16, digite apenas o número o qual você deseja o fatorial: "))
    if(num >= 0 and num <= 16):
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
        print(f"Você escolheu fazer o fatorial do número: {num}\nFatorial => {lista} = {mult}\n\n")
        escolha = str(input("Deseja realizar uma nova operação fatorial? S/N  "))
        if(escolha == 'S' or escolha == 's'):
          continue
        elif(escolha == 'N' or escolha == 'n'):
          os.system("cls")
          print("Volte sempre! :)")
          break
        else:
          os.system("cls")
          print("Comando inválido!!! Tente novamente.\n\n")
      else:
        os.system("cls")
        print("Número inválido. Tente novamente!\n\n")
    else:
      print("Número fora do intervalo estabelecido!!! Tente novamente.\n\n")
  except ValueError:
    os.system("cls")
    print("Você digitou algo errado. Tente novamente!\n\n")