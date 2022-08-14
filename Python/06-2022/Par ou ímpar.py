print("Descubra se o número é par ou ímpar!\n")
try:
  numero = int(input("Digite um número: "))
  resto = numero%2
  if(resto == 0):
    print("O número é par!")
  else:
    print("O número é ímpar!")
except ValueError:
  print("Você digitou algo errado! Tente novamente.")
