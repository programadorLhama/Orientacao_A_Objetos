from .interfaces.elemento_inteface import ElementoInterface

class Elemento(ElementoInterface):
    def executar(self) -> None:
        print("Estou Executando o Elemento")
