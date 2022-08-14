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