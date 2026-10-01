class Produto:
    def __init__(self, descricao, preco_unitario, estoque):
        self._descricao = descricao
        self._preco_unitario = preco_unitario
        self._estoque = estoque

    @property
    def descricao(self):
        return self._descricao

    @property
    def preco_unitario(self):
        return self._preco_unitario

    @property
    def estoque(self):
        return self._estoque

    def decrementar_estoque(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False

