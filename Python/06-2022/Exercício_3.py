'''
3 - Crie um programa que peça uma letra e retorne o sexo do usuário.
'''

#3
letra = str(input("Digite a letra correspondente ao seu sexo(F/M/O): "))
if(letra == 'M' or letra == 'm'):
    print("Seu sexo é masculino!")
elif(letra == 'F' or letra == 'f'):
    print("Seu sexo é feminino!")
else:
    print("Seu sexo é outro/indefinido!")