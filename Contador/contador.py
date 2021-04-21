"""
    1) Escreva em Python uma classe Contador, que encapsule um valor usado
    para contagem de itens ou eventos. A classe deve oferecer métodos
    que devem:
        a) Zerar;
        b) Incrementar;
        c) Retornar o valor do contador.
"""

class Contador:
    def __init__(self, cont):
        self.cont = cont

    def zerar(self):
        if self.cont == 0:
            return

        self.cont = 0

    def incrementar(self, inc):
        self.cont += inc

    def retornar_valor(self):
        if self.cont == 0:
            print('Contador zerado.')
            return

        print(f'O valor atual do contador é {self.cont}.')

