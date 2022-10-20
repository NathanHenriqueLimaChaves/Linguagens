# criar uma classe calculadora como métodos somar, subtrair, dividir e multiplicar. Todos privados;
# método calcular passando como parâmetro operação e valores;
# método calcular terá acesso aos métodos privados;
# instanciar objeto passando como parâmetros os valores para o método calcular;

import os

print("__________Calculadora__________\n\n")

class Calculadora():
    def __init__(self, operacao, valor1, valor2):
        self.operacao = operacao.lower()
        self.valor1 = valor1
        self.valor2 = valor2
    
    def __somar(self):
        self.resultado = self.valor1 + self.valor2
        return self.resultado
    
    def __subtrair(self):
        self.resultado = self.valor1 - self.valor2
        return self.resultado
    
    def __multiplicar(self):
        self.resultado = self.valor1 * self.valor2
        return self.resultado
    
    def __dividir(self):
        self.resultado = self.valor1 / self.valor2
        return self.resultado
    
    def calcular(self):
        if(self.operacao == "somar"):
            self.__somar()
            print(f"O resultado da adição entre {self.valor1} e {self.valor2} é: {self.resultado}")
        elif(self.operacao == "subtrair"):
            self.__subtrair()
            print(f"O resultado da subtração entre {self.valor1} e {self.valor2} é: {self.resultado}")
        elif(self.operacao == "multiplicar"):
            self.__multiplicar()
            print(f"O resultado da multiplicação entre {self.valor1} e {self.valor2} é: {self.resultado}")
        elif(self.operacao == "dividir"):
            self.__dividir()
            print(f"O resultado da divisão entre {self.valor1} e {self.valor2} é: {self.resultado}")
        else:
            print("Você digitou algo errado. Tente novamente!")


teste1 = Calculadora("somar", 15, 25)
teste1.calcular()

teste2 = Calculadora("subtrair", 35, 20)
teste2.calcular()

teste3 = Calculadora("multiplicar", 15, 10)
teste3.calcular()

teste4 = Calculadora("dividir", 100, 10)
teste4.calcular()


    