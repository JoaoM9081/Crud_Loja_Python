class Produto:
    def __init__(self, nome, preco, quantidade, descontoPermitido=False):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descontoPermitido = descontoPermitido
        self.desconto_aplicado = False 

    def aplicarDesconto(self, percentual):
        if not self.desconto_aplicado:
            self.preco -= self.preco * (percentual / 100)
            self.desconto_aplicado = True  
        else:
            print(f"Desconto já foi aplicado ao produto {self.nome}.")

    def reduzirEstoque(self, quantidade):
        self.quantidade -= quantidade

    def estaDisponivel(self, quantidade):
        return self.quantidade >= quantidade