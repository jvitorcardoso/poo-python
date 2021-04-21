"""
    class DataBase, com 4 funções embutidas:
        - insert_client -> Insere um novo cliente no banco (caso o ID já exista, sobrescreve o nome relacionado a este ID);
        - list_client -> Lista os clientes cadastrados;
        - list_names -> Lista apenas os nomes dos clientes;
        - drop_client -> Apaga os dados de um cliente (precisa apenas informar o ID)
"""

class DataBase:
    def __init__(self):
        self._data = {}

    def insert_client(self, id, name):
        if 'clientes' not in self._data:
            self._data['clientes'] = {id: name}
        else:
            self._data['clientes'].update({id: name})

    def list_client(self):
        for id, name in self._data.items():
            print(f'{id} {name}')

    def list_names(self):
        total = 0
        for id in self._data.values():
            print(f'{id.values()}')
            for _x in enumerate(id):
                total += 1
        print(f'Total de clientes cadastrados: {total}')
    
    def drop_client(self, id):
        del self._data['clientes'][id]
