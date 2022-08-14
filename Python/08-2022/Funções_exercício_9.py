import os
from datetime import date, datetime
lista = []
while True:
    try:
        print("*----------Data por extenso----------*\n\n")
        print("OBS - Digite 0 para sair do programa!\n")
        data = str(input("Digite uma data(DD/MM/AAAA): "))
        os.system("cls")
        if(data == '0'):
            os.system("cls")
            print("Volte sempre! :)")
            break
        else:
            print(f"A data escolhida, {data}, por extenso é igual a:\n")
            lista = data.split('/')
            dia = int(lista[0])
            mes = int(lista[1])
            ano = int(lista[2])
            lista.clear()
            lista.append(dia)
            lista.append(mes)
            lista.append(ano)
            #print(len(lista))
            #print(type(len(lista)))
            if(len(lista) == 3):
                if(lista[2] > 0 and lista[2] <= 9999):
                    if(lista[1] > 0 and lista[1] <= 12):
                        def dataConversao(lista):        
                            lista_mes = {1: "Janeiro",2: "Fevereiro",3: "Março",4: "Abril",5: "Maio",6: "Junho",7: "Julho",8: "Agosto",9: "Setembro",10: "Outubro",11: "Novembro",12: "Dezembro"}
                            print(f"{lista[0]} de {lista_mes[lista[1]]} de {lista[2]}.")
                        dataConversao(lista)
                        os.system("pause")
                        os.system("cls")
                    else:
                        os.system("cls")
                        print("Mês impossível. Tente novamente!\n")
                else:
                    os.system("cls")
                    print("Ano impossível. Tente novamente!\n")
            else:
                os.system("cls")
                print("Data inválida. Tente novamente!\n")
    except ValueError:
        os.system("cls")
        print("Você digitou algo errado. Tente novamente!\n")   