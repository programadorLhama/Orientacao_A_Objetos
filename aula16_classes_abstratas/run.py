from abc import ABC, abstractmethod

class Pessoa(ABC):  # Classe abstrata não possui objetos - so pode ser mãe (herança)
    def correr(self):
        print("A pessoa esta correndo de manha")

    @abstractmethod # Classe filha DEVE criar um metodo trabalhar
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print("O Professor esta dando aula")

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print("O Cozinheiro esta dando cozinhando")

p1 = Professor()
p1.trabalhar()
p1.correr()