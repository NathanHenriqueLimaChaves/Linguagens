print("O número é inteiro ou decimal? Descubra!\n")
try:
  numero = float(input("Digite um número: "))
  numero_round = round(numero)
  if(numero_round == numero):
    print("É um número inteiro!")
  else:
    print("É um número decimal!")
except ValueError:
  print("Você digitou algo que não é um número! Tente novamente.")
