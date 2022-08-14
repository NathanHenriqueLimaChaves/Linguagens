'''
1 - Crie um algoritmo que receba um ano e retorne se oano é bissexto ou não.
'''

print("É ano bissexto? Descubra:\n")
while True:
    try:
        ano = int(input("Digite um ano: "))
        ano_div1 = ano%4
        if(ano_div1 == 0):
            ano_div2 = ano%100
            if(ano_div2 == 0):
                ano_div3 = ano%400
                if(ano_div3 == 0):
                    print(f"O ano de {ano} é bissexto!")
                else:
                    print(f"O ano de {ano} não é bissexto!")
            else:
                print(f"O ano de {ano} é bissexto!")
        else:
            print(f"O ano de {ano} não é bissexto!")
    except ValueError:
        print("Digite um número válido!")