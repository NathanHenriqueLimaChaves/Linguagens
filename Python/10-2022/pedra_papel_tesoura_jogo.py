import random
import os

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
lista = [pedra, papel, tesoura]

print("__________Pedra, Papel ou Tesoura__________\n\n")
print("Vamos jogar um jogo? ;)")
os.system("pause")
os.system("cls")
while True:
    try:
        escolha = int(
            input("Qual a sua escolha? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
        if (escolha == 0):
            print(f"Você escolheu:\n{pedra}")
            computador = random.randint(0, 2)
            print(f"O computador escolheu:\n{lista[computador]}")
            if (escolha == computador):
                print("Empate!!!\n\n")
                os.system("pause")
                os.system("cls")
            elif (computador == 1):
                print("Você perdeu!!!\n\n")
                os.system("pause")
                os.system("cls")
            elif (computador == 2):
                print("Você ganhou!!!\n\n")
                os.system("pause")
                os.system("cls")
        elif (escolha == 1):
            print(f"Você escolheu:\n{papel}")
            computador = random.randint(0, 2)
            print(f"O computador escolheu:\n{lista[computador]}")
            if (escolha == computador):
                print("Empate!!!\n\n")
                os.system("pause")
                os.system("cls")
            elif (computador == 0):
                print("Você ganhou!!!\n\n")
                os.system("pause")
                os.system("cls")
            elif (computador == 2):
                print("Você perdeu!!!\n\n")
                os.system("pause")
                os.system("cls")
        elif (escolha == 2):
            print(f"Você escolheu:\n{tesoura}")
            computador = random.randint(0, 2)
            print(f"O computador escolheu:\n{lista[computador]}")
            if (escolha == computador):
                print("Empate!!!\n\n")
                os.system("pause")
                os.system("cls")
            elif (computador == 0):
                print("Você perdeu!!!\n\n")
                os.system("pause")
                os.system("cls")
            elif (computador == 1):
                print("Você ganhou!!!\n\n")
                os.system("pause")
                os.system("cls")
        else:
            os.system("cls")
            print("Desculpa, escolha não encontrada! Tente novamente\n\n")
    except ValueError:
        os.system("cls")
        print("Por favor, apenas números inteiros!\n\n")
