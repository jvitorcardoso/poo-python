class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percent):
        self.preco = self.preco - (self.preco * (percent / 100))

    # GETTER
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    # SETTER
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            valor = valor.title()

        self._nome = valor


p1 = Produto('VIDEOGAME', 1500)
print(p1.nome, p1.preco)
p2 = Produto('TELEVISÃO', 950)
p2.desconto(10)
print(p2.nome, p2.preco)
p3 = Produto('CAMA', 'R$700')
print(p3.nome, p3.preco)