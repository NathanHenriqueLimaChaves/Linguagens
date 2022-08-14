'''
1-Crie um programa que peça dois núeros e informe qual é o maior ou se são iguais.
'''

#1
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
if(a > b):
    print("'a' é maior que 'b'")
    print(a, ">", b)
elif(b > a):
    print("'b' é maior que 'a'")
    print(b, ">", a)
else:
    print("Os valores são iguais!")
    print(a,"=",b)