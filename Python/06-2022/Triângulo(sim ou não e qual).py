try:
    ladoa = float(input("Digite o valor do primeiro lado: "))
    ladob = float(input("Digite o valor do segundo lado: "))
    ladoc = float(input("Digite o valor do terceiro lado: "))
    if(ladoa+ladob > ladoc and ladoa+ladoc > ladob and ladob+ladoc > ladoa):
        print("É um triângulo!")
        if(ladoa == ladob and ladob == ladoc):
            print("É Equilátero!")
        elif(ladoa == ladob and ladob != ladoc):
            print("É Isósceles!")
        elif(ladob == ladoc and ladoc != ladoa):
            print("É Isósceles!")
        elif(ladoa == ladoc and ladoa != ladob):
            print("É Isósceles!")
        elif(ladoa != ladob and ladoa != ladoc and ladob != ladoc):
            print("É Escaleno!")
    else:
        print("Não é um triângulo!") 
except ValueError:
    print("Você digitou algo que não é um número. Tente novamente.") 
    