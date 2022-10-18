

class Forma():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def calculaArea(self):
        self.area = self.base*self.altura
        print(f"A área é igual a {self.area} unidades.")
    
    def calculaPerimetro(self):
        self.perimetro = 2*self.base + 2*self.altura
        print(f"O perímetro é igual a {self.perimetro} unidades.")


class Triangulo(Retangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def calculaArea(self):
        self.area = (self.base*self.altura)/2
        print(f"A área é igual a {self.area} unidades.")
    
    def calculaPerimetro(self):
        self.perimetro = 3*self.base
        print(f"O perímetro é igual a {self.perimetro} unidades.")


forma1 = Retangulo(20, 15)
forma2 = Triangulo(30, 15)

print(isinstance(forma1, Forma))
print(isinstance(forma2, Forma))

print(forma1.calculaArea())
print(forma2.calculaArea())

print(forma2.calculaPerimetro())