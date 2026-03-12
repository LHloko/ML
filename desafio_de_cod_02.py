## Entrada
# uma string contendo dois valores separados por espaço: o valor do pedido (um número inteiro) e a prioridade do pedido (uma palavra, podendo ser "alta", "media" ou "baixa")
## Saida 
#

# Recebe a entrada do usuário (valor e prioridade)
entrada = input().strip()
valor_str, prioridade = entrada.split()
valor = int(valor_str)

# TODO: Implemente a lógica condicional para decidir entre "aprovado", "revisao" ou "rejeitado" conforme as regras do desafio.
"""O sistema deve aprovar automaticamente pedidos de valor até 1000 com prioridade "alta" ou "media". Pedidos acima de 1000 com prioridade "alta" devem ser encaminhados para revisão. Todos os demais pedidos devem ser rejeitados.
"""

status = "rejeitado"

# Pedidos ate 1000
if valor <= 1000:
    if prioridade == "alta" or prioridade == "media":
        status = "aprovado"
# Pedidos acima de 1000
else:
    if prioridade == "alta":
        status = "revisao"
    
print(status)