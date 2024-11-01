from elementos.interfaces.elemento_inteface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2

class Principal:
    def __init__(self, elem: ElementoInterface) -> None:
        self.__elem = elem

    def run(self) -> None:
        self.__elem.executar()
        print("Estou finalizando na classe principal")


el = Elemento2()
cl1 = Principal(el)
cl1.run()
