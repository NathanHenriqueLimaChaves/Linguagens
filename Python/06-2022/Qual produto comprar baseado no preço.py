while True:
    try:        
        print("Está com dúvida? Nós resolvenos isso por você!\n")
        a = float(input("Preço do primeiro produto: R$"))
        if(a >= 0):
            b = float(input("Preço do segundo produto: R$"))
            if(b >= 0):
                c = float(input("Preço do terceiro produto: R$"))
                if(c >= 0):
                    if(a > b and a > c and b < c): #A>C>B
                        print("O produto 1, possui o maior preço = R$",a)
                        print("O produto 2, possui o menor preço = R$",b)
                        print("Compre o segundo produto!")
                    elif(a > b and a > c and c < b): #A>B>C
                        print("O produto 1, possui o maior preço = R$",a)
                        print("O produto 3, possui o menor preço = R$",c)
                        print("Compre o terceiro produto!")
                    elif(b > a and b > c and a < c): #B>C>A
                        print("O produto 2, possui o maior preço = R$",b)
                        print("O produto 1, possui o menor preço = R$",a)
                        print("Compre o primeiro produto!")
                    elif(b > a and b > c and c < a): #B>A>C
                        print("O produto 2, possui o maior preço = R$",b)
                        print("O produto 3, possui o menor preço = R$",c)
                        print("Compre o terceiro produto!")
                    elif(c > a and c > b and a < b): #C>B>A
                        print("O produto 3, possui o maior preço = R$",c)
                        print("O produto 1, possui o menor preço = R$",a)
                        print("Compre o primeiro produto!")
                    elif(c > a and c > b and b < a): #C>A>B
                        print("O produto 3, possui o maior preço = R$",c)
                        print("O produto 2, possui o menor preço = R$",b)
                        print("Compre o segundo produto!")
                    elif(a == b and a > c): #A=B>C
                        print(f"O primeiro e o segundo produto possuem o mesmo preço e são mais caros. Compre o terceiro produto, de valor R${c}.")
                    elif(a == b and a < c): #A=B<C
                        print(f"O primeiro e o segundo produto possuem o mesmo preço e são mais baratos do que o terceiro produto. Escolha entre os dois primeiros.")
                    elif(a == c and a > b): #A=C>B
                        print(f"O primeiro e o terceiro produto possuem o mesmo preço e são mais caros. Compre o segundo produto, de valor R${b}.")
                    elif(a == c and a < b): #A=C<B
                        print(f"O primeiro e o terceiro produto possuem o mesmo preço e são mais baratos do que o segundo produto. Escolha entre o primeiro e o terceiro produto.")
                    elif(b == c and b > a): #B=C>A
                        print(f"O segundo e o terceiro produto possuem o mesmo preço e são mais caros do que o primeiro produto. Compre o primeiro produto, de valor R${a}.")
                    elif(b == c and b < a): #B=C<A
                        print(f"O segundo e o terceiro produto possuem o mesmo preço e são mais baratos do que o primeiro produto. Escolha entre o segundo e terceiro produto.")
                    elif(a == b and a == c): #A=B=C
                        print("Os produtos possuem o mesmo preço. Escolha o que desejar!")
                    break 
                else:
                    print("Não existe produto com valor negativo. Tente novamente!\n")
            else:
                print("Não existe produto com valor negativo. Tente novamente!\n")
        else:
            print("Não existe produto com valor negativo. Tente novamente!\n")
    except ValueError:
        print("Você digitou algo que não é um número. Tente novamente!\n")