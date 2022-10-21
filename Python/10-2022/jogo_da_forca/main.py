import os
import random
from arte_jogo_da_forca import logo, estagios
from lista_palavras import lista_palavras


palavra_escolhida = random.choice(lista_palavras)
tamanho_palavra = len(palavra_escolhida)

fim_do_jogo = False
vidas = 6

print(logo)
print("__________Regras do Jogo__________\n\n")
print("1)As palavras não possuem acento;\n2)A letra 'ç' está incluida;\n3)Você possui 6 vida. Cada erro, perde uma;")
os.system("pause")
os.system("cls")

display = []
lista_letras = []
for _ in range(tamanho_palavra):
    display += "_"

while not fim_do_jogo:
    tentativa = input("Escolha uma letra: ").lower()
    os.system("cls")
    if tentativa not in lista_letras:
        lista_letras.append(tentativa)
    else:
        print(f"Você já tentou essa letra: {tentativa}. Tente outra!")

    for posicao in range(tamanho_palavra):
        letra = palavra_escolhida[posicao]
        if letra == tentativa:
            display[posicao] = letra

    if tentativa not in palavra_escolhida:
        print(
            f"A palavra não possui a letra {tentativa} . Você perdeu uma vida!")
        vidas -= 1
        if vidas == 0:
            fim_do_jogo = True
            os.system("cls")
            print("##### Você perdeu! #####")
            print(f"A palavra era: {palavra_escolhida}\n")

    print(f"{' '.join(display)}")

    if "_" not in display:
        fim_do_jogo = True
        os.system("cls")
        print("##### Você ganhou! #####")
        print(f"Palavra: {palavra_escolhida}")

    print(estagios[vidas])
