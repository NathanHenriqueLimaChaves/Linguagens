print("Bem-vindo(a)!")
nome = str(input("Nome do aluno: "))
materia = str(input("Materia: "))
while True:
    try:
        nota = float(input("Digite uma nota(entre 0 e 10):  "))
        if(nota < 0 or nota > 10):
            print("Você digitou uma nota fora do intervalo permitido. Tente novamente.")
        else:
            print(f"A nota digitada foi {nota}")
            break
    except ValueError:
        print("Você digitou algo errado! Tente novamente.")
