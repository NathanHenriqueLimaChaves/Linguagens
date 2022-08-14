'''
2 - Crie um algoritmo que receba uma data e retorne se a mesma é possível.
'''

print("Digite uma data no formato dd/mm/aaaa e eu te direi se essa data é possível!\n")
try:
    dia = int(input("Digite um dia: "))
    mes = int(input("Digite um mês: "))
    ano = int(input("Digite um ano: "))
    data = (f"{dia}/{mes}/{ano}")
    if(ano > 0):
        if(dia <= 0 or dia > 31):
            print(f"O dia fornecido,{dia}, não existe!")
            print(f"Logo, a data {data} não é possível.")
        elif(dia > 0 and dia <= 31):
            if(mes <= 0 or mes > 12):
                print(f"O mês fornecido,{mes}, não existe!")
                print(f"Logo, a data {data} não é possível!.")
            elif(mes == 2):
                ano_div1 = ano%4
                if(ano_div1 == 0):
                    ano_div2 = ano%100
                    if(ano_div2 == 0):
                        ano_div3 = ano%400
                        if(ano_div3 == 0):
                            if(dia <= 29):
                                print(f"A data {data} é possível!")
                            else:
                                print(f"A data {data} não é possível")
                    else:
                        if(dia <= 29):
                            print(f"A data {data} é possível!")
                        else:
                            print(f"A data {data} não é possível!")
                else:
                    if(dia <= 28):
                        print(f"A data {data} é possível!")
                    else:
                        print(f"A data {data} não é possível!")
            else:
                if(mes == 4 or mes == 6 or mes == 9 or mes == 11):
                    if(dia <= 30):
                        print(f"A data {data} é possível!")
                    else:
                        print(f"A data {data} não é possível!")
                elif(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                    if(dia <= 31):
                        print(f"A data {data} é possível!")
    elif(ano <= 0):
        print("O ano fornecido não é possível")
        print(f"Logo, a data {data} não é possível.")
except ValueError:
    print("Você digitou algo que não é um número inteiro. Tente novamente!")