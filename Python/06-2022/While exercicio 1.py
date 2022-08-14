numero = int(input("Digite um número: "))
valor = numero
lista = []
count = 0
while(valor > 0):
    valor = valor - 1
    lista.append(valor)
    count += 1
       
else:
    print(lista)
    print(f"O número chegou a 0 depois de  vezes.")
