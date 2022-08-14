while True:
    try:
        a = float(input("Digite um número: "))
        b = float(input("Digite um número: "))
        c = float(input("Digite um número: "))
        if(a > b and a > c):
            print("O número ",a," é o maior número!")
        elif(b > a and b > c):
            print("O número ",b," é o maior número!")
        elif(c > a and c > b):
            print("O número ",c," é o maior número!")
        elif(a == b and a == c):
            print("Os números são iguais")
    except ValueError:
        print("Você não digitou um número! Tente novamente.") 

