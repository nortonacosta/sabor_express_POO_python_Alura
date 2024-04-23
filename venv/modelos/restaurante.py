from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do restaurante'.ljust(25)} '
              f'| {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f' {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} '
                  f'| {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 10:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        ''' Retorna a média das avaliações
        Input: uma lista de avaliações
        Output: média das avaliações

        '''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas)
        return media


    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}:\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R$ {str(item._preco).ljust(10)} | Descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R$ {str(item._preco).ljust(10)} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)





# def classificavel(self):
#     media = self.media_avaliacao
#     if isinstance(media, str):
#         print("Não há avaliações disponíveis.")
#         return
#
#     if media > 9:
#         print('★★★★★')
#     elif 7.5 < media <= 9:
#         print('★★★★')
#     elif 4.5 < media <= 7.5:
#         print('★★★')
#     elif 2.5 < media <= 4.5:
#         print('★★')
#     elif media <= 2.5:
#         print('★')









