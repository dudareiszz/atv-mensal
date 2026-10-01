from datetime import datetime
from itemVenda import ItemVenda


class Venda:
    def __init__(self):
        self._data = datetime.now()
        self._valor_total = 0
        self._itens = []

    @property
    def valor_total(self):
        return self._valor_total

    def adicionar_item(self, produto, quantidade):
        if produto.decrementar_estoque(quantidade):
            item = ItemVenda(produto, quantidade)
            self._itens.append(item)
            self.calcular_total()
            return True
        return False

    def remover_item(self, produto):
        for item in self._itens:
            if item.produto == produto:
                produto._estoque += item.quantidade
                self._itens.remove(item)
                self.calcular_total()
                return True
        return False

    def calcular_total(self):
        total = 0
        for item in self._itens:
            total += item.calcular_subtotal()
        self._valor_total = total
        return total


        



        
