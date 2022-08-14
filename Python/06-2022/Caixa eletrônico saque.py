try:
  print("Bem-vindo(a) ao caixa eletrônico!\n")
  print("Por enquanto, só temos disponível a opção de saque!")
  print("Valor mínimo: R$10,00 / Valor máximo: R$600,00")
  saque_inicial = int(input("Digite o valor do saque: "))
  if(saque_inicial >= 10 and saque_inicial <= 600):
      cem = int(saque_inicial/100)
      saque = saque_inicial - (cem*100)
      cinquenta = int(saque/50)
      saque = saque - (cinquenta*50)
      dez = int(saque/10)
      saque = saque - (dez*10)
      cinco = int(saque/5)
      saque = saque - (cinco*5)
      um = int(saque/1)
      saque = saque - (um*1)
      print(f"Você irá receber R${saque_inicial},00 nas seguintes notas: {cem} de 100,00; {cinquenta} de 50,00; {dez} de 10,00; {cinco} de 5,00 e {um} de 1,00.")
      print("Retire o dinheiro abaixo.")
      print("Tenha um ótimo dia!")
  else:
      print("Valor indiponível!Tente novamente.")
except ValueError:
  print("Você digitou algo errado! Tente novamente.")
