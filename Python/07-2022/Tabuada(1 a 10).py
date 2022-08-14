print("Bem vindo a tabuada fácil!\n\n")
try:
  num = int(input("Digite o número que você deseja saber a tabuada: "))
  if (num > 0 and num < 11):
    for i in range(num,num+1):
      print("\n")
      for j in range(1,11):
        print(i,"X",j,"=", i*j)
  else:
    print("Número fora do intervalo possível. Tente novamente!")
except ValueError:
  print("Você digitou algo errado. Tente novamente!")
print("\n-------------------------------\n")