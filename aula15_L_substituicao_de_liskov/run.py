# Quebra do principio de Liskov
class Animal:
    def alimentar(self):
        print("O Animal esta se alimentando")

class Cachorro(Animal):
    def latir(self):
        print("O Cachorro esta latindo")

class Peixe(Cachorro):
    def nadar(self):
        print("O Peixe esta nadando")

    def latir(self): # comportamento diferente
        raise Exception("Peixe nao Late")
    

def verificar_animal(animal: any):
    animal.latir()

obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()
verificar_animal(obj3)
