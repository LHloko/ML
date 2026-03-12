## Entrada 
# O sistema recebe o valor total de um pedido
# E o percentual de desconto a ser aplicado
## Saida 
# Calcular o valor final do pedido após o desconto, garantindo precisão e agilidade

# Lê a linha de entrada e separa os valores
entrada = input().strip().split()
valor_total = float(entrada[0])
percentual_desconto = int(entrada[1])

# TODO: Calcule o valor final do pedido após aplicar o desconto percentual
desconto = percentual_desconto/100
valor_descontado = valor_total * desconto
valor_final = valor_total - valor_descontado

# Imprima o valor final com duas casas decimais
print(f"{valor_final:.2f}")