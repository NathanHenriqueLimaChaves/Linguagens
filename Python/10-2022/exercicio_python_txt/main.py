"""Um gerente contábil armazena todos os dados do funcionário da empresa Philco. Cada funcionário sob sua
responsabilidade possui um id, um nome e um salário. Crie um arquivo funcionario.txt que armazena o id e 
o nome de seus funcionários. Crie um arquivo salario.txt que possui o id do funcionario e seu  respectivo
salário. Cadastre, para teste, cinco funcionários. Escreva um programa que permita consultar o salário de
cada funcionário, a partir do seu nome ou id. O programa deve receber como entrada o id/nome e imprimir a
linha correspondente ao nome no arquivo salario.txt"""
import os

while True:
    try:
        print("_____Consulta_____\n\n")
        print("Consultar por:\n1)ID\n2)Nome\n3)Sair")
        escolha = int(input("Sua escolha: "))
        os.system("cls")

        texto_separado = []
        cadastro = ""
        if(escolha == 1):    
            num_id = input("Digite o ID do funcionário: ")
            with open("salario.txt", 'r', encoding='utf-8') as arquivo:
                texto = arquivo.readlines()
            for linha in texto:
                if num_id in linha:
                    print(linha)
                    cadastro += linha
            texto_separado = cadastro.split()  
            num_id = texto_separado[0]
            with open("funcionario.txt", 'r', encoding='utf-8') as arquivo:
                texto = arquivo.readlines()
            for linha in texto:
                if num_id in linha:
                    print(linha)
            os.system("pause")
            os.system("cls")
        elif(escolha == 2):
            nome = str(input("Digite o nome do funcionário: "))
            with open("funcionario.txt", 'r', encoding='utf-8') as arquivo:
                texto = arquivo.readlines()
            for linha in texto:
                if nome in linha:
                    print(linha)
                    cadastro += linha        
            texto_separado = cadastro.split()  
            num_id = texto_separado[0]
            with open("salario.txt", 'r', encoding='utf-8') as arquivo:
                texto = arquivo.readlines()
            for linha in texto:
                if num_id in linha:
                    print(linha)
            os.system("pause")
            os.system("cls")
        elif(escolha == 3):
            os.system("cls")
            print("Volte sempre!\n")
            break
        else:
            os.system("cls")
            print("Escolha inválida!Tente novamente.\n\n")
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente.\n")

