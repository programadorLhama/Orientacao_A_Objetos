class MinhaClasse:
    def __init__(self, info, elem): # metodo construtor é o primeiro!
        self.atributo_1 = "meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "a"]
        self.atributo_novo = info
        print(self.atributo_novo)

    def metodo_1(self):
        print("minha acao1")
        print("minha acao2")
        print(self.atributo_2)
        return "Ola Mundo"

    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)

# objeto        # classe -> instanciamos um objeto
minha_classe = MinhaClasse("info aqui no construtor", 213)

minha_classe.metodo_2(3)
