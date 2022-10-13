import os

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("__________Bem-vind(a) a Ilha do Tesouro.__________")
print("Sua missão é encontrar o tesouro.\n\n")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
os.system("pause")
os.system("cls")
while True:
    escolha1 = str(input(
        "Você está em um cruzamento. Para onde você quer ir? Digite 'esquerda' ou 'direita'\n"))
    escolha1_low = escolha1.lower()
    os.system("cls")
    if (escolha1_low == 'esquerda'):
        print("Vcoê caiu num buraco e morreu. Game over!")
        break
    elif (escolha1_low == 'direita'):
        escolha2 = str(input(
            "Você chegou a um lago. Tem um pequena ilha no meio do lago. Digite 'esperar' para esperar pelo barco. Digite 'nadar' para nadar até a ilha.\n"))
        escolha2_low = escolha2.lower()
        os.system("cls")
        if (escolha2_low == 'esperar'):
            print("Você chegou em segurança a ilha.")
            escolha3 = str(input(
                "Você encontrou uma casa que tem três portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?\n"))
            escolha3_low = escolha3.lower()
            os.system("cls")
            if (escolha3_low == 'vermelha'):
                print("Um grupo de zombies matou você. Game over!")
                break
            elif (escolha3_low == 'azul'):
                print(
                    "Você entrou dentro de uma sala cheia de gás venenoso. Você morreu. Game over!")
                break
            elif (escolha3_low == 'amarela'):
                print("Você encontrou um baú misterioso")
                escolha4 = str(input("Abrir? S ou N\n"))
                escolha4_low = escolha4.lower()
                os.system("cls")
                if (escolha4_low == 's'):
                    escolha5 = str(input("Você tem certeza disso? S ou N\n"))
                    escolha5_low = escolha5.lower()
                    os.system("cls")
                    if (escolha5_low == 's'):
                        print(
                            "Você abriu o baú e encontrou um grande tesouro.\nParabéns. Você está RICO agora. Game over :)")
                    elif (escolha5_low == 'n'):
                        print(
                            "Você chegou perto mas decidiu continuar pobre :( Game over!")
                        break
                    else:
                        os.system("cls")
                        print("Escolha inválida. Tente novamente :)\n\n")
                elif (escolha4_low == 'n'):
                    print(
                        "Você ficou com medo e decidiu voltar para casa. Você está seguro agora.\nPobre mas seguro. Game over!")
                    break
                else:
                    os.system("cls")
                    print("Escolha inválida. Tente novamente :)\n\n")
            else:
                os.system("cls")
                print("Escolha inválida. Tente novamente :)\n\n")
        elif (escolha2_low == 'nadar'):
            print("O rio estava cheio de crocodilos. Você morreu. Game over!")
            break
        else:
            os.system("cls")
            print("Escolha inválida. Tente novamente :)\n\n")

    else:
        os.system("cls")
        print("Escolha inválida. Tente novamente :)\n\n")
