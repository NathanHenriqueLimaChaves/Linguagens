while True:
    try:
        a = int(input("Digite um número inteiro: "))
        b = int(input("Digite um número inteiro: "))
        c = int(input("Digite um número inteiro: "))
        if(a > b and a > c and b < c): #A>C>B
            print("Em ordem decrescente: ",a,">",c,">",b)
            print("Em ordem crescente: ",b,"<",c,"<",a)
        elif(a > b and a > c and c < b): #A>B>C
            print("Em ordem decrescente: ",a,">",b,">",c)
            print("Em ordem crescente: ",c,"<",b,"<",a)
        elif(b > a and b > c and a < c): #B>C>A
            print("Em ordem decrescente: ",b,">",c,">",a)
            print("Em ordem crescente: ",a,"<",c,"<",b)
        elif(b > a and b > c and c < a): #B>A>C
            print("Em ordem decrescente: ",b,">",a,">",c)
            print("Em ordem crescente: ",c,"<",a,"<",b)
        elif(c > a and c > b and a < b): #C>B>A
            print("Em ordem decrescente: ",c,">",b,">",a)
            print("Em ordem crescente: ",a,"<",b,"<",c)
        elif(c > a and c > b and b < a): #C>A>B
            print("Em ordem decrescente: ",c,">",a,">",b)
            print("Em ordem crescente: ",b,"<",a,"<",c)
        elif(a == b and a > c): #A=B>C
            print("Em ordem decrescente: ",a,"=",b,">",c)
            print("Em ordem crescente: ",c,"<",b,"=",a)
        elif(a == b and a < c): #C>B=A
            print("Em ordem decrescente: ",c,">",b,"=",a)
            print("Em ordem crescente: ",a,"=",b,"<",c)
        elif(a == c and a > b): #A=C>B
            print("Em ordem decrescente: ",a,"=",c,">",b)
            print("Em ordem crescente: ",b,"<",c,"=",a)
        elif(a == c and a < b): #B>C=A
            print("Em ordem decrescente: ",b,">",c,"=",a)
            print("Em ordem crescente: ",a,"=",c,"<",b)
        elif(b == c and b > a): #B=C>A
            print("Em ordem decrescente: ",b,"=",c,">",a)
            print("Em ordem crescente: ",a,"<",c,"=",b)
        elif(b == c and b < a): #A>B=C
            print("Em ordem decrescente: ",a,">",b,"=",c)
            print("Em ordem crescente: ",b,"=",c,"<",a)
        elif(a == b and a == c):
            print(f"Os números são iguais: {a}={b}={c}") 
        break
    except ValueError:
        print("Você digitou algo que não é um número inteiro. Tente novamente!")