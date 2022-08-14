'''
4 - Peça uma letra e retorne se é vogal ou consoante.
'''

#4
letra1 = str(input("Digite uma letra: "))
if(letra1 == 'a' or letra1 == 'A' or letra1 == 'e' or letra1 == 'E' or letra1 == 'i' or letra1 == "I" or letra1 == "o" or letra1 == "O" or letra1 == "u" or letra1 == "U"):
    print("É uma vogal")
   
else:
    print("É uma consoante")