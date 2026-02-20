'''Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um métdo que mostre uma etiqueta de preço do produto.'''

from rich import print
from rich.panel import Panel

class Produto:
    """
Representa um produto de uma loja.

Armazena o nome e preço do produto e
Permite exibir uma etiqueta de preco
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        etiqueta = Panel(f'{self.nome}'.center(36) + '-' * 36 + f'R${self.preco:,.2f}'.center(36), title='Produto', width=40)
        print(etiqueta)

p1 = Produto('iPhone 17 Pro Max', 25000.85)
p2 = Produto('Notebook Gamer', 8000)

p1.etiqueta()
p2.etiqueta()