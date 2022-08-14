#Início da lista de exercícios Python => dia 07/06/2022
#Continuação da lista de exercícios Python => dia 08/06/2022
#CÓDIGOS CORRIGIDOS 1.0 => dia 18/06/2022 e 19/06/2022#

#5(FEITO)
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


#6(FEITO)
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

#7(FEITO)
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

#8(FEITO)
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

#9(FEITO)
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

#10(FEITO)
turno = str(input("Qual o seu turno:M/V/N? "))
if(turno == 'M' or turno == 'm'):
    print("Bom dia!")
elif(turno == 'V' or turno == 'v'):
    print("Boa tarde!")
elif(turno == 'N' or turno == 'n'):
    print("Boa noite!")
else:
    print("Comando inválido!") 

#11(FEITO)
while True:
    try:
        print("Bem-vindo(a) a calculadora rápida de salário!\n")
        salario_atual = float(input("Digite o seu salário atual(apenas números): R$"))
        if(salario_atual >= 0):
            if(salario_atual < 280):
                reajuste = 20/100
                salario_final = salario_atual+(salario_atual*reajuste)
                print("Seu salário antes do reajuste era: R$",salario_atual)
                print("O reajuste para você foi de 20%")
                print("O valor de acréscimo em seu salário foi de R$",salario_atual*reajuste)
                print("O seu novo salário é de R$",salario_final)
            elif(salario_atual >= 280 and salario_atual < 700):
                reajuste = 15/100
                salario_final = salario_atual+(salario_atual*reajuste)
                print("Seu salário antes do reajuste era: R$",salario_atual)
                print("O reajuste para você foi de 15%")
                print("O valor de acréscimo em seu salário foi de R$",salario_atual*reajuste)
                print("O seu novo salário é de R$",salario_final)
            elif(salario_atual >= 700 and salario_atual < 1500):
                reajuste = 10/100
                salario_final = salario_atual+(salario_atual*reajuste)
                print("Seu salário antes do reajuste era: R$",salario_atual)
                print("O reajuste para você foi de 10%")
                print("O valor de acréscimo em seu salário foi de R$",salario_atual*reajuste)
                print("O seu novo salário é de R$",salario_final)
            elif(salario_atual >= 1500):
                reajuste = 5/100
                salario_final = salario_atual+(salario_atual*reajuste)
                print("Seu salário antes do reajuste era: R$",salario_atual)
                print("O reajuste para você foi de 5%")
                print("O valor de acréscimo em seu salário foi de R$",salario_atual*reajuste)
                print("O seu novo salário é de R$",salario_final)
            break
        else:
            print("Salário inválido! Tente novamente.")
    except ValueError:
        print("Você digitou algo errado. Tente novamente!\n")

#12(FEITO)
print("Bem vindo(a)\n")
nome = str(input("Qual o seu nome: "))
try:
    horas = int(input("Quantas horas você trabalhou esse mês: "))
    if(horas >= 0):
        valor = float(input("Qual o valor de sua hora de trabalho? "))
        if(valor >= 0):
            salario_bruto = horas*valor
            if(salario_bruto <= 900):
                ir = 0/100
                ir_valor = salario_bruto*ir
                sindicato = 3/100
                sindicato_valor = salario_bruto*sindicato
                fgts = salario_bruto*11/100
                descontos = ir_valor+sindicato_valor
                salario_liquido = salario_bruto-descontos
                print("Salário Bruto: (",horas,"*",valor,")","    : R$",salario_bruto)
                print("(-) IR(0)","     : R$",ir_valor)
                print("(-) INSS(3%)","    : R$",sindicato_valor)
                print("FGTS(11%)","      : R$",fgts) #FGTS não entra no cálculo final
                print("Total de descontos      : R$",descontos)
                print("Salário Líquido      : R$",salario_liquido)
            elif(salario_bruto > 900 and salario_bruto <= 1500):
                ir = 5/100
                ir_valor = salario_bruto*ir
                sindicato = 3/100
                sindicato_valor = salario_bruto*sindicato
                fgts = salario_bruto*11/100
                descontos = ir_valor+sindicato_valor
                salario_liquido = salario_bruto-descontos
                print("Salário Bruto: (",horas,"*",valor,")","    : R$",salario_bruto)
                print("(-) IR(5%)","     : R$",ir_valor)
                print("(-) INSS(3%)","    : R$",sindicato_valor)
                print("FGTS(11%)","      : R$",fgts) #FGTS não entra no cálculo final
                print("Total de descontos      : R$",descontos)
                print("Salário Líquido      : R$",salario_liquido)
            elif(salario_bruto > 1500 and salario_bruto <= 2500):
                ir = 10/100
                ir_valor = salario_bruto*ir
                sindicato = 3/100
                sindicato_valor = salario_bruto*sindicato
                fgts = salario_bruto*11/100
                descontos = ir_valor+sindicato_valor
                salario_liquido = salario_bruto-descontos
                print("Salário Bruto: (",horas,"*",valor,")","    : R$",salario_bruto)
                print("(-) IR(10%)","     : R$",ir_valor)
                print("(-) INSS(3%)","    : R$",sindicato_valor)
                print("FGTS(11%)","      : R$",fgts) #FGTS não entra no cálculo final
                print("Total de descontos      : R$",descontos)
                print("Salário Líquido      : R$",salario_liquido)
            elif(salario_bruto > 2500):
                ir = 20/100
                ir_valor = salario_bruto*ir
                sindicato = 3/100
                sindicato_valor = salario_bruto*sindicato
                fgts = salario_bruto*11/100
                descontos = ir_valor+sindicato_valor
                salario_liquido = salario_bruto-descontos
                print("Salário Bruto: (",horas,"*",valor,")","    : R$",salario_bruto)
                print("(-) IR(20%)","     : R$",ir_valor)
                print("(-) INSS(3%)","    : R$",sindicato_valor)
                print("FGTS(11%)","      : R$",fgts) #FGTS não entra no cálculo final
                print("Total de descontos      : R$",descontos)
                print("Salário Líquido      : R$",salario_liquido)
        else:
            print("Valor inválido. Tente novamente!")
    else:
        print("Valor inválido. Tente novamente!")
        
except ValueError:
    print("Você digitou algo errado! Tente novamente.")

#13(FEITO) 
try:
    numero = int(input("Digite um número: "))
    if(numero == 1):
        print("Domingo!!!")
    elif(numero == 2):
        print("Segunda!!!")
    elif(numero == 3):
        print("Terça!!!")
    elif(numero == 4):
        print("Quarta!!!")
    elif(numero == 5):
        print("Quinta!!!")
    elif(numero == 6):
        print("Sexta!!!")
    elif(numero == 7):
        print("Sabado!!!")
    else:
        print("Número inválido") 
except ValueError:
    print("Você digitou algo errado. Tente novamente!")

#14(FEITO)
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
    

#15(FEITO) 
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
    




