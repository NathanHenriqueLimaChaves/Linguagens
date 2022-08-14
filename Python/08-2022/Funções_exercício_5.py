'''
5 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago por
uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o
número de dias em atraso e passar estes valores para a função valorPagamento, que calculará
o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então
exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro va-
lor de prestação e assim continuar até que seja informado um valor igual a zero para a pres-
tação . Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que con-
terá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago
é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando
houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''
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
            def valorPagamento (valor):
                total = round(valor,2)
                print(f"O total a pagar é R${total} reais!")
                lista_valor.append(total)
                os.system("pause")
                os.system("cls")
            valorPagamento(valor)
            lista_dias.append(dias)
        else:
            os.system("cls")
            def valorPagamento (valor, dias):
                total = round((valor)+(3/100*valor)+(1/1000*dias),2)
                print(f"O total a pagar é R${total} reais!")
                lista_valor.append(total)
                os.system("pause")
                os.system("cls")
            valorPagamento(valor, dias)
            lista_dias.append(dias)
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente!\n")
print("RELATÓRIO:\n")
final = 0
for i in lista_valor:
    print(f"\t-R${i} reais;")
    final += i
print(f"\tTotal do dia: R${round(final,2)} reais.")
os.system("pause")