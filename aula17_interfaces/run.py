from abc import ABC, abstractmethod

class Trabalhador(ABC): # Interface

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def horario_de_almoco(self) -> None: pass


class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O Professor esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor esta indo para casa")

    def horario_de_almoco(self) -> None:
        print("O Professor esta almocando")

class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print("O Engenheiro esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O Engenheiro esta indo para casa")

    def horario_de_almoco(self) -> None:
        print("O Engenheiro esta almocando")


def comunicar_o_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print("Comunicar o trabalhador para ir para casa")
    trabalhador.ir_para_casa()

p1 = Professor()
p2 = Engenheiro()

comunicar_o_trabalhador(p1)
print()

comunicar_o_trabalhador(p2)