from abc import ABC, abstractmethod

class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def consultar_beneficios(self) -> None: pass

class TrabalhadorTemporario(ABC):
    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O Professor esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor esta indo para casa")

    def consultar_beneficios(self) -> None:
        print("Consultando beneficios da CLT")

class ProfessorSubstituto(TrabalhadorTemporario):
    def trabalhar(self) -> None:
        print("O Professor Substituto esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor Substituto esta indo para casa")

p2 = ProfessorSubstituto()