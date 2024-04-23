from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco,descricao, sabor, tamanho):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.sabor = sabor
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.03