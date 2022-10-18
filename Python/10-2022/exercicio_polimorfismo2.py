

class Funcionario():
    def __init__(self, nome ,salario):
        self.nome = nome
        self.salario = salario
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.salario
        return self.salario_funcionario
    
    def calculaSalarioAnual(self):
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual
    
class Engenheiro(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.salario + (self.salario*20/100)
        return self.salario_funcionario
    
    def calculaSalarioAnual(self):
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.salario + (self.salario*30/100)
        return self.salario_funcionario
    
    def calculaSalarioAnual(self):
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual

class Analista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calculaSalarioMensal(self):
        self.salario_funcionario = self.salario + (self.salario*25/100)
        return self.salario_funcionario
    
    def calculaSalarioAnual(self):
        self.salario_anual = self.salario_funcionario*12
        return self.salario_anual

engenheiro_1 = Engenheiro("Terry", 3500)
print(isinstance(engenheiro_1, Funcionario))
print(f"O salário mensal é de: R${engenheiro_1.calculaSalarioMensal()} reais.")
print(f"O salário anual é de: R${engenheiro_1.calculaSalarioAnual()} reais.")


desenvolvedor_1 = Desenvolvedor("Nathan", 5500)
print(isinstance(desenvolvedor_1, Funcionario))
print(f"O salário mensal é de: R${desenvolvedor_1.calculaSalarioMensal()} reais.")
print(f"O salário anual é de: R${desenvolvedor_1.calculaSalarioAnual()} reais.")


analista_1 = Analista("Precioso", 6500)
print(isinstance(analista_1, Funcionario))
print(f"O salário mensal é de: R${analista_1.calculaSalarioMensal()} reais.")
print(f"O salário anual é de: R${analista_1.calculaSalarioAnual()} reais.")
