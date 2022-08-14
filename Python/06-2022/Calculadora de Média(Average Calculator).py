#Atividade 5/Exercise 5
print("Bem-vindo(a) ao cálculo de média!\n")
while True:
    try:
        nota1 = float(input("Digite a nota 1: "))
        if(nota1 >= 0 and nota1 <= 10):
             print(f"Nota 1 = {nota1}") 
        else:
            print("Essa nota é impossível. Tente novamente.")
            break     
    except ValueError:
        print("Por favor, digite algo válido. Tente novamente!")
        break
    try:
        nota2 = float(input("Digite a nota 2: "))
        if(nota2 >= 0 and nota2 <= 10):
            print(f"Nota 2 = {nota2}")
        else:
            print("Essa nota é impossível. Tente novamente.")
            break     
    except ValueError:
        print("Por favor, digite algo válido. Tente novamente!")
        break
    else:
        media = (nota1+nota2)/2
        if(media == 10):
            print("A média foi de ", media,"\n","Aluno aprovado com honras!Parabéns")
        elif(media >= 7 and media < 10):
            print("A média foi de ", media,"\n","Aluno aprovado!")
        elif(media < 7 and media >= 0):
            print("A média foi de ", media,"\n","Aluno reprovado!")
        else:
            print("Média inválida! Tente novamente.")
        break
