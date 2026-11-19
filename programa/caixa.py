
interface = "caixa aberto"
produto = "produto: "
rs = "R$"
interaçao = "Deseja adicionar mais itens? [S/N]:"
resumo_compra = "RESUMO DA COMPRA"
pagamento = "Forma de pagamento (1 - Dinheiro | 2 - Cartão): "
total = "Valor final com desconto: "
# variaveis

estoque = {
    "sku01": {"nome": "mause", "valor": 5000, "quantidade": 2},
    "sku02": {"nome": "teclado", "valor": 1000, "quantidade": 1},
    "sku03": {"nome": "camisa",  "valor": 1900, "tamanho": 170, "quantidade":6},
}

print(33*"=")
print(interface)
print(33*"=")
# cliente

cliente = input("digite seu nome: ")
print(f"bem vindo {cliente}, qual vai ser sua compra?")
print(f"{cliente}, essas sao as chave dos produtos escolha!: [sku01],[sku02][sku03]")
print(33*"=")
escolha_produto = estoque.keys()

escolha_produto = input(f"{cliente}, escolha um produto com essas keys: " .strip().lower())

print(estoque[escolha_produto])