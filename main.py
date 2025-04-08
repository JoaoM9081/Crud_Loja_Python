from Loja import Loja

def menu():
    loja = Loja()
    while True:
        print("\n--- MENU LOJA ---")
        print("1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Ver carrinho")
        print("4. Aplicar desconto em produto")
        print("5. Finalizar compra")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.exibirProdutos()

        elif opcao == "2":
            loja.exibirProdutos()
            try:
                i = int(input("Digite o número do produto: ")) - 1
                q = int(input("Quantidade: "))
                if q > 0:
                    loja.adicionarAoCarrinho(i, q)
                else:
                    print("A quantidade deve ser maior que zero.")
            except:
                print("Entrada inválida.")

        elif opcao == "3":
            loja.carrinho.listarItens()
            print(f"Total: R$ {loja.carrinho.calcularTotal():.2f}")

        elif opcao == "4":
            loja.exibirProdutos()
            try:
                i = int(input("Produto para aplicar desconto: ")) - 1
                d = float(input("Percentual de desconto: "))
                if d > 0:
                    loja.aplicarDescontoProduto(i, d)
                else:
                    print("Desconto deve ser maior que zero.")
            except:
                print("Entrada inválida.")

        elif opcao == "5":
            if loja.carrinho.itens:
                print("Formas de pagamento:")
                print("1. Dinheiro/Pix (10% desconto)")
                print("2. Cartão à vista (sem desconto)")
                print("3. Cartão parcelado (5% acréscimo)")
                metodo = input("Escolha o método: ")
                loja.simularPagamento(metodo)
            else:
                print("Carrinho vazio.")

        elif opcao == "6":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")

menu()