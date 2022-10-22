

class Funcionario():
    def __init__(self, nome ,salario):
        self.nome = nome
        self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario
        return self.__salario

func1 = Funcionario("Nathan", 7000)

with open("dados.txt", 'w') as arquivo:
    arquivo.write("Nome: "+ func1.nome + "\n" +"Salario: "+str(func1.getSalario()))


