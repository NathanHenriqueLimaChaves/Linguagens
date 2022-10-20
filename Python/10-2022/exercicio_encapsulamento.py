

class Funcionario():
    def __init__(self, nome , salario):
        self.nome = nome
        self.__salario = salario
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.__salario
        return self.salario_funcionario
    
    def __calculaSalarioAnual(self):
        self.calculaSalarioMensal()
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual
    
    def retornaCalculoSalarioAnual(self):
        self.__calculaSalarioAnual()
        print(f"Você ganha anualmente: R${self.salario_anual} reais.")
    
class Engenheiro(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.__salario = salario
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.__salario + (self.__salario*20/100)
        return self.salario_funcionario
    
    def __calculaSalarioAnual(self):
        self.calculaSalarioMensal()
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual
    
    def retornaCalculoSalarioAnual(self):
        self.__calculaSalarioAnual()
        print(f"Você ganha anualmente: R${self.salario_anual} reais.")
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.salario + (self.salario*30/100)
        return self.salario_funcionario
    
    def __calculaSalarioAnual(self):
        self.calculaSalarioMensal()
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual
    
    def retornaCalculoSalarioAnual(self):
        self.__calculaSalarioAnual()
        print(f"Você ganha anualmente: R${self.salario_anual} reais.")

class Analista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.salario + (self.salario*25/100)
        return self.salario_funcionario
    
    def __calculaSalarioAnual(self):
        self.calculaSalarioMensal()
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual

    def retornaCalculoSalarioAnual(self):
        self.__calculaSalarioAnual()
        print(f"Você ganha anualmente: R${self.salario_anual} reais.")

funcionario1 = Funcionario("Nathan", 5000)
funcionario1.retornaCalculoSalarioAnual()

engenheiro1 = Engenheiro("José", 7500)
engenheiro1.retornaCalculoSalarioAnual()