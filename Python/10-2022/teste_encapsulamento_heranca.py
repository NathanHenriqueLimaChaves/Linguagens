

class Funcionario():
    def __init__(self, id_func, nome, idade, cpf, cargo, salario):
        self.__idfunc = id_func
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.cargo = cargo
        self.__salario = salario

    def __salarioMensal(self):
        self.salarioMensal = self.__salario
        return self.salarioMensal

    def __salarioAnual(self):
        self.salarioAnual = self.salarioMensal * 12
        return self.salarioAnual

    def getSalarios(self):
        self.__salarioMensal()
        self.__salarioAnual()
        print(f"ID funcionário: {self.__idfunc}\nFuncionário: {self.nome}\nCPF: {self.__cpf}\nSalário mensal: R${self.salarioMensal}\nSalário anual: R${self.salarioAnual}")


class Desenvolvedor(Funcionario):
    def __init__(self, id_func, nome, idade, cpf, cargo, salario):
        super().__init__(id_func, nome, idade, cpf, cargo, salario)
        self.__idfunc = id_func
        self.__cpf = cpf
        self.__salario = salario

    def __salarioMensal(self):
        self.salarioMensal = self.__salario + (self.__salario * 15/100)
        return self.salarioMensal

    def __salarioAnual(self):
        self.salarioAnual = self.salarioMensal * 12
        return self.salarioAnual

    def getSalarios(self):
        self.__salarioMensal()
        self.__salarioAnual()
        print(f"ID funcionário: {self.__idfunc}\nFuncionário: {self.nome}\nCPF: {self.__cpf}\nSalário mensal: R${self.salarioMensal}\nSalário anual: R${self.salarioAnual}")


class Analista(Funcionario):
    def __init__(self, id_func, nome, idade, cpf, cargo, salario):
        super().__init__(id_func, nome, idade, cpf, cargo, salario)
        self.__idfunc = id_func
        self.__cpf = cpf
        self.__salario = salario

    def __salarioMensal(self):
        self.salarioMensal = self.__salario + (self.__salario * 45/100)
        return self.salarioMensal

    def __salarioAnual(self):
        self.salarioAnual = self.salarioMensal * 12
        return self.salarioAnual

    def getSalarios(self):
        self.__salarioMensal()
        self.__salarioAnual()
        print(f"ID funcionário: {self.__idfunc}\nFuncionário: {self.nome}\nCPF: {self.__cpf}\nSalário mensal: R${self.salarioMensal}\nSalário anual: R${self.salarioAnual}")


func1 = Desenvolvedor(1, "Nathan", 24, "24583829472", "Desenvolvedor", 5000)
func1.getSalarios()
print("\n\n")
func2 = Analista(5, "Thiago", 35, "27579583822", "Analista", 7600)
func2.getSalarios()
