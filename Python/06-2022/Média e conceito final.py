print("Bem vindo(a) ao sistema de controle de notas!\n")
aluno = str(input("Digite o nome do(a) aluno(a): "))
materia = str(input("Digite a matéria: "))
while True:
    try:
        nota1 = float(input("Digite a primeira nota do aluno(a): "))
        nota2 = float(input("Digite a segunda nota do aluno(a): "))
        media = (nota1+nota2)/2
        if(media >= 9 and media <= 10):
            print("A nota 1 foi ",nota1)
            print("A nota 2 foi ",nota2)
            print("A média foi ",media)
            print("A média recebeu o conceito 'A'")
            print("Aluno APROVADO!")
        elif(media >= 7.5 and media < 9):
            print("A nota 1 foi ",nota1)
            print("A nota 2 foi ",nota2)
            print("A média foi ",media)
            print("A média recebeu o conceito 'B'")
            print("Aluno APROVADO!")
        elif(media >= 6 and media < 7.5):
            print("A nota 1 foi ",nota1)
            print("A nota 2 foi ",nota2)
            print("A média foi ",media)
            print("A média recebeu o conceito 'C'")
            print("Aluno APROVADO!")
        elif(media >= 4 and media < 6):
            print("A nota 1 foi ",nota1)
            print("A nota 2 foi ",nota2)
            print("A média foi ",media)
            print("A média recebeu o conceito 'D'")
            print("Aluno REPROVADO!")
        elif(media < 4 and media >= 0):
            print("A nota 1 foi ",nota1)
            print("A nota 2 foi ",nota2)
            print("A média foi ",media)
            print("A média recebeu o conceito 'E'")
            print("Aluno REPROVADO!")
        else:
            print("Média inválida")
        break
    except ValueError:
        print("Você digitou algo errado. Tente novamente!")