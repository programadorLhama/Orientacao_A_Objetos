from .interfaces.elemento_inteface import ElementoInterface

class Elemento2(ElementoInterface):
    def executar(self) -> None:
        print("Estou Executando o Elemento Alternativo")
