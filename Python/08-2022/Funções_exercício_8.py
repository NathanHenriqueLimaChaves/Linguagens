'''
8 - Jogo de Craps. Faça um programa de um jogo de Craps. O jogador lança um par de dados, ob-
tendo um valor entre 2 e 12. Se, na primeira rodada, ele tirar 7 ou 11, ele é "natural" e 
ganhou. Se ele tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e ele perdeu.
Se, na primeira rodada, ele fizer um 4, 5, 6, 8, 9 ou 10, ele fez um "Ponto". O objetivo dele
agora é continuar jogando os dados até tirar este número novamente. Entretanto, se ele tirar 
um 7 antes de tirar o mesmo "Ponto" novamente, ele perde.
'''
import os
from random import randint
lista = []
while True:
    try:
        print("*----------Jogo de Craps----------*\n\n")
        print("Pronto para rodar os dados?")
        os.system("pause")
        os.system("cls")
        def dados():
            print("-----RODADA 1-----")
            dado1 = randint(1,6)
            dado2 = randint(1,6)
            total = dado1+dado2
            print(f"Dado 1 : {dado1}\nDado 2 : {dado2}\nTotal = {dado1+dado2}")
            os.system("pause")       
            if(total == 7 or total == 11):
                print("RESULTADO:\n-------VOCÊ GANHOU-------\n")
                os.system("pause")
                os.system("cls")
            elif(total == 2 or total == 3 or total == 12):
                print("RESULTADO:\n-------CRAPSSSSSSSS---VOCÊ PERDEU-------\n")
                os.system("pause")
                os.system("cls")
            elif(total == 4 or total == 5 or total == 6 or total == 8 or total == 9 or total == 10):
                print("RESULTADO:\n-------Você fez um Ponto-------\n")
                print("Se fizer o mesmo ponto novamente, VOCÊ VENCE!")
                lista.append(total)
                os.system("pause")
                os.system("cls")
                n = 1
                while True:
                    n += 1
                    print(f"-----RODADA {n}-----\n\n")
                    dado1 = randint(1,6)
                    dado2 = randint(1,6)
                    total = dado1+dado2
                    print(f"Dado 1 : {dado1}\nDado 2 : {dado2}\nTotal = {total}")
                    os.system("pause") 
                    if(lista[0] == total):
                        print("RESULTADO:\n-------VOCÊ GANHOU-------\n")
                        print("Você fez o mesmo Ponto novamente e venceu o jogo!!!Parabéns.")
                        lista.clear()
                        os.system("pause")
                        os.system("cls")
                        break
                    elif(total == 7):
                        print("RESULTADO:\n-------VOCÊ PERDEU-------\n")
                        print("Você tirou 7 e isso fez você perder! :(")
                        lista.clear()
                        break
                    else:
                        print("RESULTADO:\n-------JOGO CONTINUA-------\n")
                        os.system("pause")
                        os.system("cls")
                        continue       
                os.system("pause")
                os.system("cls")
        dados()
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente!\n")