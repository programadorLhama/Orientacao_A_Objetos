class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f"enviando mensagem: {mensagem}")

    def abrir_emails(self) -> None:
        print("Abrindo os Emails...")

    def abrir_youtube(self) -> None:
        print("Abrindo Youtube...")


class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.__celular = celular

    def pedir_pizza(self) -> None:
        print("Buscando o celular...")
        print("definindo o sabor...")
        self.__celular.enviar_mensagem("quero uma de calabreza")
        print("aguardando a chegada")

    def estudar(self) -> None:
        print("Sentando no computador")
        self.__celular.abrir_youtube()
        print("Anotando o conteudo")


android = Celular("samsung")
iphone = Celular("iphone")

reginaldo = Pessoa(android)
marlene = Pessoa(iphone)

reginaldo.pedir_pizza()
print()
marlene.estudar()