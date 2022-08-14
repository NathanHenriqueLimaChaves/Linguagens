from multiprocessing.sharedctypes import Value

import os


print ("*--------Menu Abrec!--------*\n")
while True:
    try:
        print("*--------Menu Principal--------*\n")
        print("[1] Pacientes\n[2] Cuidadores\n[3] Estoque\n[4] Colaboradores\n[5] Fornecedores\n[6] Cursos\n[7] Sair\n")
        escolha = int(input("Sua escolha: "))
        os.system("cls")
        if(escolha == 1):
            print("--------Pacientes!--------")
            while True:
                try:
                    print("1-Incluir\n2-Excluir\n3-Relatório\n4-Voltar\n")          
                    escolha_2 = int(input("Sua escolha: "))
                    os.system("cls")
                    if (escolha_2 == 1):
                        nome = str(input("Insira o nome: "))
                        endereco = str(input("Insira endereço: "))
                        telefone = str(input("Insira telefone: "))
                        e_mail = str(input("Insira email: "))
                        sexo = str(input("Insira sexo: "))
                        nascimento = str(input("Insira nascimento: ")) 
                        tipo = str(input("Insira tipo de paciente: "))
                        renda = str(input("Insira renda: "))
                        doenca = str(input("Insira doença: "))
                        codigo_nis = str(input("Insira código nis: "))
                        os.system("cls")
                        print("Dados salvos!\n\n")                        
                    elif(escolha_2 == 2):
                        nome = None
                        endereco = None
                        telefone = None
                        e_mail = None
                        sexo = None
                        nascimento = None
                        tipo = None
                        renda = None
                        doenca = None
                        codigo_nis = None
                        os.system("cls")
                        print("Dados excluidos!\n\n")
                    elif(escolha_2 == 3):
                        print(f"Nome:{nome}\nEndereço:{endereco}\nTelefone:{telefone}\nEmail:{e_mail}\nSexo:{sexo}\nNascimento:{nascimento}\nTipo de paciente:{tipo}\nRenda:{renda}\nDoença:{doenca}\nCódigo Nis:{codigo_nis}")
                        print("\n\n")
                    elif(escolha_2 == 4):
                        print("\n\n")
                        break
                except ValueError:
                    print("Opção inválida. Tente novamente!\n\n")          
        elif(escolha == 2):
            print("--------Cuidadores!--------")
            while True:
                try:
                    print("1-Incluir\n2-Excluir\n3-Relatório\n4-Voltar\n") 
                    escolha_3 = int(input("Sua escolha: "))
                    os.system("cls")
                    if (escolha_3 == 1):
                        nome = str(input("Insira o nome: "))
                        endereco = str(input("Insira endereço: "))
                        telefone = str(input("Insira telefone: "))
                        e_mail = str(input("Insira email: "))
                        sexo = str(input("Insira sexo: "))
                        nascimento = str(input("Insira nascimento: ")) 
                        renda = str(input("Insira renda: "))
                        os.system("cls")             
                        print("Dados salvos!\n\n")
                    elif(escolha_3 == 2):
                        nome = None
                        endereco = None
                        telefone = None
                        e_mail = None
                        sexo = None
                        nascimento = None
                        renda = None
                        print("Dados excluidos!\n\n")
                    elif(escolha_3 == 3):
                        print(f"Nome:{nome}\nEndereço:{endereco}\nTelefone:{telefone}\nEmail:{e_mail}\nSexo:{sexo}\nNascimento:{nascimento}\nTipo de paciente:{tipo}\nRenda:{renda}\nDoença:{doenca}\nCódigo Nis:{codigo_nis}")
                        print("\n\n")
                    elif(escolha_3 == 4):
                        print("\n\n")
                        break
                except ValueError:
                    print("Opção inválida. Tente novamente!\n\n")       
        elif(escolha == 3):
            print("--------Estoque!--------")
            while True:
                try:
                    print("1-Incluir\n2-Excluir\n3-Relatório\n4-Voltar\n")                
                    escolha_4 = int(input("Sua escolha: "))
                    os.system("cls")
                    if (escolha_4 == 1):
                        cod_produto = str(input("Insira o Código do Produto: ")) 
                        desc_produto = str(input("Insira a descrição do produto: "))
                        valor_produto = str(input("Insira o valor do Produto: "))
                        quant_estoque = int(input("Insira a quantidade do Estoque: "))
                        categ_estoque = str(input("Insira a categoria do estoque: "))
                        obs = str(input("Observações: "))
                        os.system("cls")
                        print("Dados salvos\n\n")
                    elif(escolha_4 == 2):
                        cod_produto = None 
                        desc_produto = None
                        valor_produto = None
                        quant_estoque = None
                        categ_estoque = None
                        obs = None
                        print("Dados excluidos\n\n")
                    elif(escolha_4 == 3):
                        print(f"Código do Produto:{cod_produto}\nDescrição do produto:{desc_produto}\nValor do Produto:{valor_produto}\nCategoria do estoque:{categ_estoque}\nObservação:{obs}")
                        print("\n\n")
                    elif(escolha_4 == 4):
                        print("\n\n")
                        break
                except ValueError:
                    print("Opção inválida. Tente novamente!\n\n")
        elif(escolha == 4):
            print("--------Colaboradores!--------")
            while True:
                try:
                    print("1-Incluir\n2-Excluir\n3-Relatório\n4-Voltar\n")           
                    escolha_5 = int(input("Sua escolha: "))
                    os.system("cls")
                    if (escolha_5 == 1):
                        nome = str(input("Insira o nome: "))
                        endereco = str(input("Insira endereço: "))
                        telefone = str(input("Insira telefone: "))
                        e_mail = str(input("Insira email: "))
                        sexo = str(input("Insira sexo: "))
                        nascimento = str(input("Insira nascimento: ")) 
                        tipo = str(input("Insira o tipo de colaborador: ")) 
                        funcao = str(input("Função: "))
                        os.system("cls")            
                        print("Dados salvos!\n\n") 
                    elif(escolha_5 == 2):
                        nome = None
                        endereco = None
                        telefone = None
                        e_mail = None
                        sexo = None
                        nascimento = None
                        tipo = None
                        funcao = None
                        print("Dados excluidos\n\n")
                    elif(escolha_5 == 3):
                        print(f"Nome:{nome}\nEndereço:{endereco}\nTelefone:{telefone}\nEmail:{e_mail}\nSexo:{sexo}\nNascimento:{nascimento}\nTipo de colaborador:{tipo}\nfunção:{funcao}")
                        print("\n\n")
                    elif(escolha_5 == 4):
                        print("\n\n")
                        break
                except ValueError:
                    print("Opção inválida. Tente novamente!\n\n")       
        elif(escolha == 5):
            print("--------Fornecedores!--------")
            while True:
                try:
                    print("1-Incluir\n2-Excluir\n3-Relatório\n4-Voltar\n")           
                    escolha_6 = int(input("Sua escolha: "))
                    os.system("cls")
                    if(escolha_6 == 1):
                        nome = str(input("Insira o nome: "))
                        endereco = str(input("Insira endereço: "))
                        telefone = str(input("Insira telefone: "))
                        e_mail = str(input("Insira email: "))
                        cnpj = str(input("Insira o CNPJ: "))
                        obs = str(input("Insira Observações: ")) 
                        tipo = str(input("Insira o tipo de Fornecedor: ")) 
                        produto = str(input("Produto: "))
                        os.system("cls")            
                        print("Dados salvos!\n\n") 
                    elif(escolha_6 == 2):
                        nome = None
                        endereco = None
                        telefone = None
                        e_mail = None
                        sexo = None
                        nascimento = None
                        tipo = None
                        funcao = None
                        print("Dados excluidos\n\n")
                    elif(escolha_6 == 3):
                        print(f"Nome:{nome}\nEndereço:{endereco}\nTelefone:{telefone}\nEmail:{e_mail}\nSexo:{sexo}\nNascimento:{nascimento}\nTipo de colaborador:{tipo}\nfunção:{funcao}")
                        print("\n\n")
                    elif(escolha_6 == 4):
                        print("\n\n")
                        break
                except ValueError:
                    print("Opção inválida. Tente novamente!")       
        elif(escolha == 6):
            print("--------Cursos!--------")
            while True:
                try:
                    print("1-Incluir\n2-Excluir\n3-Relatório\n4-Voltar\n")             
                    escolha_7 = int(input("Sua escolha: "))
                    os.system("cls")
                    if (escolha_7 == 1):
                        nome = str(input("Nome do curso: "))
                        data = str(input("Data: "))
                        horario = str(input("Horário: "))
                        vagas = int(input("Numero de Vagas: "))
                        professor = str(input("Professor(a): "))
                        duracao = str(input("Duração: "))
                        os.system("cls")
                        print("Dados salvos\n\n ")
                    elif(escolha_7 == 2):
                        nome = None
                        data = None
                        horario = None
                        vagas = None
                        professor = None
                        duracao = None
                        print("Dados excluídos\n\n ")
                    elif(escolha_7 == 3):
                        print(f"Nome:{nome}\nData:{data}\nHorário:{horario}\nVagas:{vagas}\nProfessor:{professor}\nDuração:{duracao}\n")
                    elif(escolha_7 == 4):
                        print("\n\n")
                        break
                except ValueError:
                    print("Opção inválida. Tente novamente!\n\n")
        elif(escolha == 7):
            print("Volte Sempre!:)")
            break  
        else:
            os.system("cls")
            print("Não existe esse comando. Tente novamente\n\n")
    except ValueError:
        os.system("cls")
        print("Comando inválido!\n\n")
