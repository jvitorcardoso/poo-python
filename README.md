# poo-python

## Welcome to my Python world!

Primeiros passos na construção de códigos limpos e bem estruturados, todos orientados a objetos.

* Sumário:
  - **BaseData** <--- class DataBase, com 4 funções embutidas:
        - *insert_client* -> Insere um novo cliente no banco (caso o ID já exista, sobrescreve o nome relacionado a este ID);
            - *list_client* -> Lista os clientes cadastrados;
            - *list_names* -> Lista apenas os nomes dos clientes;
            - *drop_client* -> Apaga os dados de um cliente (precisa apenas informar o ID)
  
  * **Contador** <--- Programa que constrói um contador mega básico em Python a partir de uma classe *Contador*, e que encapsula um valor usado para contagem de itens ou eventos. A classe deve oferecer métodos que devem:
  
    ​    *a) Zerar;*
  
    ​    *b) Incrementar;*
  
    ​    *c) Retornar o valor do contador*.
  
  * **Produtos** <--- Cria uma classe *Produto* com os atributos de nome e preço. Tem os métodos de _desconto_ e um basicão das propriedades **getter** e **setter**.