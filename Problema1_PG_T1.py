'''Todo restaurante, embora por lei não possa obrigar o cliente
a pagar, cobra 10% do valor da conta como taxa de serviço.
Elabore um programa que leia o valor gasto com as despesas
realizadas em um restaurante e exiba o valor total com a taxa
de serviço(conforme exemplo)

Exemplo:
Por favor digite o valor da conta(em reais): 75
Valor da taxa de serviço: 7.5 reais
Valor Total da conta(com taxa de serviço): 82.5 reais
'''
print('*** Sistema de cálculo de conta em restaurante. ***')
valor_da_conta = input('Por favor digite o valor da conta(em reais):')
valor_da_conta = float(valor_da_conta)
taxa_de_servico = valor_da_conta * 0.1
valor_total_da_conta = valor_da_conta + taxa_de_servico
mensagem = "Valor da taxa de serviço: "+ str(taxa_de_servico) +" reais."
print(mensagem)
print('Valor Total da conta(com taxa de serviço): '+ str(valor_total_da_conta) +" reais.")
