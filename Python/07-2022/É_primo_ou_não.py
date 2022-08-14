
print("*----------É primo ou não?----------*\n\n")
try:
  num = int(input("Digite um número inteiro: "))
  count = 0
  if(num > 1):
    for i in range(1,num+1):
      if(num % i == 0):
        count += 1
    if(count == 2):
      print("É primo!!!")
    else:
      print("Não é primo!!!")
  elif(num == 1):
    print("Não é primo!!!")
  else:
    print("Número inválido!!!")
except ValueError:
  print("Você digitou algo errado! Tente novamente.")