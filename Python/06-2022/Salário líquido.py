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