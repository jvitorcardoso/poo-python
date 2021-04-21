from Produto import Produto

p1 = Produto('VIDEOGAME', 1500)
print(p1.nome, p1.preco)
p2 = Produto('TELEVISÃO', 950)
p2.desconto(10)
print(p2.nome, p2.preco)
p3 = Produto('CAMA', 'R$700')
print(p3.nome, p3.preco)