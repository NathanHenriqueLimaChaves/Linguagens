print("Bem-vindo(a) a exponenciação rápida!\n\n")
try:
  base = int(input("Digite qual o número da base: "))
  expoente = int(input("Digite qual o número do expoente "))
  for i in range(base,base+1):
    print(base,"elevado à", expoente," = ",base**expoente)
except ValueError:
  print("Você digitou algo errado. Tente novamente!")
print("\n-------------------------------\n")