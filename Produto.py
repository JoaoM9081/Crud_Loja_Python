class Produto:
    def __init__(self, nome, preco, quantidade, descontoPermitido=False):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descontoPermitido = descontoPermitido

    def aplicarDesconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

    def reduzirEstoque(self, quantidade):
        self.quantidade -= quantidade

    def estaDisponivel(self, quantidade):
        return self.quantidade >= quantidade