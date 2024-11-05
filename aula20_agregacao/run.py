class Produto:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome
        self.__valor = valor

    def informacoes_do_produto(self) -> None:
        print(f"Produto: {self.__nome} - Valor: {self.__valor}")


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produtos(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print("Compra Finalizada!")
        print("     Produtos: ")
        for product in self.__produtos:
            product.informacoes_do_produto()


banana = Produto("banana", 3)
pera = Produto("pera", 2)
uva = Produto("uva", 4)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produtos(pera)
carrinho.adicionar_produtos(banana)
carrinho.adicionar_produtos(uva)

carrinho.finalizar_compra()
