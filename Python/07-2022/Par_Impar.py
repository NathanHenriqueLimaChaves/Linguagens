'''
Crie um programa que receberá 10 números inteiros e deverá retronar a soma desses números + quantos desses números
são par e quantos são ímpar.
'''

lista = []
par = 0
impar = 0
count = 10
while count > 0:
  lista.append(int(input("Digite dez números inteiros: ")))
  count -= 1
soma = sum(lista)
for i in lista:
  if(i % 2 == 0):
    par += 1
  else:
    impar += 1
print(f"A soma de todos os números que você digitou é igual a: {soma}\nQuantidade de números pares: {par}\nQuantidade de números ímpares: {impar}")
print("\n-------------------------------\n")