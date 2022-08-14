import os
lista_valor = []
lista_dias = []
while True:
    try:
        print("*----------Prestação de Contas----------*\n\n")
        print("OBS - Digite 0 no valor da prestação para finalizar o programa.\n")
        valor = float(input("Valor da prestação: "))
        dias = int(input("Número de dias em atraso: "))
        if(valor == 0):
            os.system("cls")
            print("Programa finalizado! Aqui está o relatório do dia:\n")
            break
        elif(valor < 0):
            os.system("cls")
            print("Valor incorreto. Digite novamente!\n")
        elif(dias == 0):
            os.system("cls")
            lista_valor.append(valor)
            lista_dias.append(dias)
            def valorPagamento (valor):
                total = valor
                print(f"O total a pagar é R${total} reais!")
                os.system("pause")
                os.system("cls")
            valorPagamento(valor)
        else:
            os.system("cls")
            lista_valor.append(valor)
            lista_dias.append(dias)
            def valorPagamento (valor, dias):
                total = (valor)+(3/100*valor)+(1/1000*dias)
                print(f"O total a pagar é R${total} reais!")
                os.system("pause")
                os.system("cls")
            valorPagamento(valor, dias)
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente!\n")
print("RELATÓRIO:\n")
final = 0
for i in lista_valor:
    print(f"\t-R${i} reais;")
    final += i
print(f"\tTotal do dia: R${final} reais.")
os.system("pause")