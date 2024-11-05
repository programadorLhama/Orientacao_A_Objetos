class Select:
    def by_id(self) -> any:
        print("Selecionando um elemento no BD")

class Insert:
    def inser_value(self) -> None:
        print("inserindo um valor no BD")


class Repositorio:
    def __init__(self) -> None:
        self.__select = Select() # composicao
        self.__insert = Insert()

    def select_by_id(self, id: int) -> any:
        self.__select.by_id()

repo = Repositorio()
repo.select_by_id(45)
