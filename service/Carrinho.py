class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionarItem(self, produto, quantidade):
        if produto.nome in self.itens:
            self.itens[produto.nome]['quantidade'] += quantidade
        else:
            self.itens[produto.nome] = {'produto': produto, 'quantidade': quantidade}

    def calcularTotal(self):
        return sum(item['produto'].preco * item['quantidade'] for item in self.itens.values())

    def listarItens(self):
        if not self.itens:
            print("Carrinho está vazio.")
        else:
            for item in self.itens.values():
                produto = item['produto']
                quantidade = item['quantidade']
                print(f"{produto.nome} - R$ {produto.preco:.2f} x {quantidade}")

    def esvaziarCarrinho(self):
        self.itens.clear()
