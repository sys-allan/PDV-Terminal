
interface = "caixa aberto"
produto = "produto: "
rs = "R$"
interaçao = "Deseja adicionar mais itens? [S/N]:"
resumo_compra = "RESUMO DA COMPRA"
pagamento = "Forma de pagamento (1 - Dinheiro | 2 - Cartão): "
total = "Valor final com desconto: "
escolha = "periferico1"
escolha2 = "periferico"
escolha3 = "roupas1"
escolha4 = "roupas"
# variaveis

estoque = {
    "periferico1": {"nome": "mause", "valor": 5000, "quantidade": 2},
    "periferico": {"nome": "teclado", "valor": 1000, "quantidade": 1},
    "roupas1": {"nome": "camisa",  "valor": 1900, "tamanho": 170, "quantidade":6},
    "roupas": {"nome": "calca",  "valor": 190, "tamanho": 170, "quantidade":3},
}

print(33*"=")
print(interface)
print(33*"=")
# cliente

cliente = input("digite seu nome: ")
print(f"bem vindo {cliente}, qual vai ser sua compra?")
print(f"{cliente}, essas sao as chave dos produtos escolha!: [roupas1],[roupas],[periferico1],[periferico]")
print(33*"=")

# escolha cliente
escolha = "" 
escolha_produto = estoque.keys()
escolha_produto = input(f"{cliente},  " .strip().lower())

print(f"voce escolheu {escolha_produto}, que custa" [5] ,"deseja continuar: "  )