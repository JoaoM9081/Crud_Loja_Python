from service.Produto import Produto
from service.Carrinho import Carrinho

class Loja:
    def __init__(self):
        self.produtos = []
        self.carrinho = Carrinho()
        self.carregarProdutosIniciais()

    def carregarProdutosIniciais(self):
        self.produtos.append(Produto("Camisa", 50.0, 10, True))
        self.produtos.append(Produto("Calça", 100.0, 5))
        self.produtos.append(Produto("Tênis", 200.0, 8, True))
        self.produtos.append(Produto("Jaqueta", 150.0, 3))
        self.produtos.append(Produto("Boné", 30.0, 12, True))
        self.produtos.append(Produto("Meia", 10.0, 30))

    def exibirProdutos(self):
        print("\nProdutos disponíveis:")
        for i, p in enumerate(self.produtos):
            if p.descontoPermitido and not p.desconto_aplicado:
                descontoInfo = " (Cupom disponível)"
            elif p.descontoPermitido and p.desconto_aplicado:
                descontoInfo = " (Desconto já aplicado)"
            else:
                descontoInfo = ""
            print(f"{i+1}. {p.nome} - R$ {p.preco:.2f} - Estoque: {p.quantidade}{descontoInfo}")


    def adicionarAoCarrinho(self, indice, quantidade):
        if 0 <= indice < len(self.produtos):
            produto = self.produtos[indice]
            quantidade_no_carrinho = self.carrinho.itens.get(produto.nome, {}).get('quantidade', 0)
            if produto.estaDisponivel(quantidade + quantidade_no_carrinho):
                self.carrinho.adicionarItem(produto, quantidade)
                print("Produto adicionado ao carrinho.")
            else:
                print("Estoque insuficiente.")
        else:
            print("Produto inválido.")


    def confirmarCompra(self):
        for item in self.carrinho.itens.values():
            produto = item['produto']
            quantidade = item['quantidade']
            produto.reduzirEstoque(quantidade)
            produto.desconto_aplicado = False  

    def aplicarDescontoProduto(self, indice, percentual):
        if 0 <= indice < len(self.produtos):
            produto = self.produtos[indice]
            if not produto.descontoPermitido:
                print("Este produto não permite descontos.")
                return
            if produto.desconto_aplicado:
                print("Desconto já foi aplicado neste produto.")
                return
            if 0 < percentual <= 75:
                produto.aplicarDesconto(percentual)
                print(f"Desconto aplicado. Novo preço: R$ {produto.preco:.2f}")
            else:
                print("Percentual do desconto inválido. Descontos permitidos apenas entre 1% a 75%")
        else:
            print("Produto inválido.")

    def simularPagamento(self, metodoPagamento):
        total = self.carrinho.calcularTotal()
        if metodoPagamento == "1":
            total *= 0.90
        elif metodoPagamento == "3":
            total *= 1.05

        print(f"Total a pagar: R$ {total:.2f}")
        try:
            valorPago = float(input("Digite o valor pago: "))
            if valorPago >= total:
                troco = valorPago - total
                print(f"Pagamento aprovado. Troco: R$ {troco:.2f}")
                self.confirmarCompra()
                self.carrinho.esvaziarCarrinho()
            else:
                print("Valor insuficiente. Compra cancelada.")
        except:
            print("Valor inválido. Compra cancelada.")