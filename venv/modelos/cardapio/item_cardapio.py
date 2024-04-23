from abc import ABC, abstractmethod

class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        ''' Aplica um desconto em um item do cardapio OBRIGATÓRIO. por ser um metodo abstrato'''
        pass