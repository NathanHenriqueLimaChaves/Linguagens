"""Faça um programa que cadastre/leia em um arquivo .txt os seguintes dados:
Nome, Sexo e Idade. Seu programa deve retornar a quantidade de pessoas do seg-
mento masculino e feminino. Seu programa deve retornar o nome das pessoas que
tem mais de 40 anos. Seu programa deve armazenar em um novo arquivo.txt todas
as pessoas entre 18 e 40 anos."""
import os

with open("cadastros.txt", "r", encoding='utf-8') as cadastros:
                texto = cadastros.readlines()
                for linha in texto:
                    respostas = linha.split(",")
                    ids = int(float(respostas[0]))
                    if(ids > ids):
                        ids = ids
                id_user = ids
                id_user += 1

print("########## Sistema de Cadastro de Usuários ##########\n\n")
with open("cadastros.txt", "a", encoding='utf-8') as cadastros:
    escolha = input("Você quer cadastrar usuários? Sim ou Não\n").lower()
    if (escolha == 'sim'):
        continuar = True
        while continuar == True:
            try:
                nome = str(input("Nome: "))
                sexo = str(input("Sexo(Feminino ou Masculino): ")).lower()
                idade = str(input("Idade: "))
            except ValueError:
                os.system("cls")
                print("Um dos dados fornecidos está incorreto! Tente novamente.")
                os.system("pause")
                os.system("cls")
                break
            cadastros.write(str(id_user))
            cadastros.write(",")
            cadastros.write(nome)
            cadastros.write(",")
            cadastros.write(sexo)
            cadastros.write(",")
            cadastros.write(idade)
            cadastros.write("\n")
            adicionar_mais = input("Adicionar mais? Sim ou Não\n").lower()
            if (adicionar_mais == 'sim'):
                os.system("cls")
                pass
            else:
                break
    else:
        pass

escolha2 = str(input(
    "Quer saber alguns fatos sobre os cadastros salvos no sistema? Sim ou Não\n")).lower()
if (escolha2 == 'sim'):
    with open("cadastros.txt", "r", encoding='utf-8') as cadastros:
        dados = cadastros.readlines()
        num_masc = 0
        num_femi = 0
        for linha in dados:
            if ("masculino" in linha):
                num_masc += 1
            elif ("feminino" in linha):
                num_femi += 1
        print(
            f"O número de pessoas do sexo masculino no sistema é: {num_masc}\nO número de pessoas do sexo feminino no sistema é: {num_femi}")
        
        acima_40 = 0
        ate_40 = 0
        nomes_acima_40 = []
        nomes_ate_40 = []
        for linha in dados:
            respostas = linha.split(",")
            idade = int(float(respostas[3]))
            if(idade > 40):
                nomes_acima_40.append(respostas[1])
                acima_40 += 1 
            elif(idade <= 40):
                nomes_ate_40.append(respostas[1])
                ate_40 += 1       
        print(
            f"Número de pessoas acima de 40 anos: {acima_40}")
        for i in nomes_acima_40:
            print(i)
        print(f"\nNúmero de pessoas até os 40 anos: {ate_40}")
        for i in nomes_ate_40:
            print(i)

else:
    print("Volte sempre!\n")

with open("cadastros_jovens.txt","w", encoding='utf-8') as arquivo2:
    with open("cadastros.txt","r", encoding='utf-8') as arquivo:
        texto = arquivo.readlines()
        for linha in texto:
            linha = linha.split(",")
            idade = int(float(linha[3]))
            if(idade > 18 and idade <= 40):
                arquivo2.write(linha[0])
                arquivo2.write(",")
                arquivo2.write(linha[1])
                arquivo2.write(",")
                arquivo2.write(linha[2])
                arquivo2.write(",")
                arquivo2.write(linha[3])

           