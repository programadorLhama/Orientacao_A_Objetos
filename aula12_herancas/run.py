class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f"O Animal esta andando pelo {self.localizacao}")


class Cachorro(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao) # se refere ao construtor da classe superior

    def latir(self) -> None:
        print("O Cachorro esta latindo")
        self.andar()

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self) -> None:
        print("O Gato esta miando")

dog = Cachorro("Chile")
dog.latir()

cat = Gato("Noruega")
cat.miar()