import os

class Atleta():
    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso
    
    def aposentar(self):
        self.aposentado = 'True'
        print("Aposentei!")
    
    def aquecer(self):
        print("Vamos lá!!!\nAquecendo...\nAquecido!!!")
    
class Corredor(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
    
    def correr(self):
        print("Correndo!!!")

class Nadador(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
    
    def nadar(self):
        print("Nadando!!!")

class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
    
    def pedalar(self):
        print("Pedalando!!!")

class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
    
    def competir(self):
        print(self.correr)
        os.system("pause")
        print(self.nadar)
        os.system("pause")
        print(self.pedalar)
        os.system("pause")
        print("Terminei!")

atleta1 = Triatleta(False, 85)
atleta2 = Triatleta(False, 79)

print(atleta1.aposentado)
print(atleta2.peso)

atleta1.aposentar()
print(atleta1.aposentado)

print(isinstance(atleta1, Triatleta))
