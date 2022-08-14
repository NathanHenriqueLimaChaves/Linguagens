'''
4 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por
exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada
todas as vezes que desejar.
'''
import os
while True:
    try:
        print("*----------Conversão de horas 24->12----------*\n\n")
        print("OBS-Se quiser sair do programa, digite 0 na hora e nos minutos!\n")
        hora = int(input("Digite a hora: "))
        minutos = int(input("Digite os minutos: "))
        if(hora < 0 or hora > 24):
            os.system("cls")
            print("Hora inválida. Tente novamente!")
        elif(minutos < 0 or minutos > 60):
            os.system("cls")
            print("Minutos inválidos. Tente novamente!")
        elif(hora == 0 and minutos == 0):
            os.system("cls")
            print("Volte sempre!!! :)")
            break
        else:
            def conversao(hora, minutos):
                if(hora >= 12):
                    hora = hora - 12
                    if(hora == 0):
                        print(f"{hora}:{minutos} A.M.")
                    print(f"{hora}:{minutos} P.M.")
                else:
                    print(f"{hora}:{minutos} A.M.")
            conversao(hora, minutos)
            os.system("pause")
            os.system("cls")
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente!\n")