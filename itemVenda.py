class ItemVenda:
    def __init__(self, produto, quantidade):
        self._produto = produto
        self._quantidade = quantidade
        self._valor_item = produto.preco_unitario

    @property
    def produto(self):
        return self._produto

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def valor_item(self):
        return self._valor_item

    def calcular_subtotal(self):
        return self.quantidade * self.valor_item
