
interface = "caixa aberto"
produto = "produto: "
rs = "R$"
interaçao = "Deseja adicionar mais itens? [S/N]:"
resumo_compra = "RESUMO DA COMPRA"
pagamento = "Forma de pagamento (1 - Dinheiro | 2 - Cartão): "
total = "Valor final com desconto: "
# variaveis

estoque = {
    "sku01": {
        "nome": "mause", "valor": 5000, "quantidade": 2,
        
    "sku02": {
        "nome": "teclado", "valor": 1000, "quantidade": 1,
        
     "sku03": {
         "nome": "gabinete", "valor": 7000, "quantidade": 11,
         
       "sku04": {
           "nome": "fans", "valor": 1500, "quantidade": 9000,
       }  
     }    
    }
#acaba aqui
    }
  
}

print(33*"=")
print(interface)
print(33*"=")
# cliente
cliente = input("digite seu nome: ")
print(f"bem vindo {cliente}, qual vai ser sua compra?")