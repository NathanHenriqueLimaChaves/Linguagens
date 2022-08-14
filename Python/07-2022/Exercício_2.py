try:
  num1 = int(input("Digite um número inteiro: "))
  num2= int(input("Digite outro número inteiro: "))
  if num1 > num2:
    for i in range(num2+1,num1):
      print(i)
    soma = (num1 + num2)
    print(f"A soma dos números {num1} e {num2} é igual a: ",soma)
  elif num2 > num1:
    for i in range(num1+1,num2):
      print(i)
    soma = (num1 + num2)
    print(f"A soma dos números {num1} e {num2} é igual a: ",soma)
except ValueError:
  print("Você digitou algo errado. Tente novamente!")
print("\n-------------------------------\n")