while True:
    try:
        a = float(input("Digite um número: "))
        b = float(input("Digite um número: "))
        c = float(input("Digite um número: "))
        if(a > b and a > c and b < c):   #A>C>B
            print("O número ",a," é o maior número!")
            print("O número ",b," é o menor número!")
        elif(a > b and a > c and c < b): #A>B>C
            print("O número ",a," é o maior número!")
            print("O número ",c," é o menor número!")
        elif(b > a and b > c and a < c): #B>C>A
            print("O número ",b," é o maior número!")
            print("O número ",a," é o menor número!")
        elif(b > a and b > c and c < a): #B>A>C
            print("O número ",b," é o maior número!")
            print("O número ",c," é o menor número!")
        elif(c > a and c > b and a < b): #C>B>A
            print("O número ",c," é o maior número!")
            print("O número ",a," é o menor número!")
        elif(c > a and c > b and b < a): #C>A>B
            print("O número ",c," é o maior número!")
            print("O número ",b," é o menor número!")
        elif(a == b and a > c): #A=B>C
            print(f"{a} e {b} são iguais e maiores do que {c}")
        elif(a == b and a < c): #A=B<C
            print(f"{a} e {b} são iguais e menores do que {c}")
        elif(a == c and a > b): #A=C>B
            print(f"{a} e {c} são iguais e maiores do que {b}")
        elif(a == c and a < b): #A=C<B
            print(f"{a} e {c} são iguais e menores do que {b}")
        elif(b == c and b > a): #B=C>A
            print(f"{b} e {c} são iguais e maiores do que {a}")
        elif(b == c and b < a): #B=C<A
            print(f"{b} e {c} são iguais e menores do que {a}")
        elif(a == b and a == c): #A=B=C
            print("Os números são iguais")
        break 
    except ValueError:
        print("Você não digitou um número! Tente novamente.")
        