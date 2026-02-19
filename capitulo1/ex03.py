def pedido():
  nome = input("Digite seu nome: ")
  produto = input("Digite o produto solicitado: ")
  quantidade = int(input("Digite a quantidade: "))
  valor = float(input("Digite o valor do produto: "))
  return nome, produto, quantidade, valor

nome, produto, quantidade, valor = pedido()
print(f"Pedido confirmado: {produto} \nValor total: R${valor * quantidade:.2f} \nObrigado pela preferência {nome}!")

