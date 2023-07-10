'''
Desenvolva um programa que calcule o preço a pagar (com imposto) pelo
fornecimento de energia elétrica. O programa deve perguntar a quantidade
de energia consumida (em kWh) e o tipo de instalação:
• ‘R’ ou ‘r’ (Residências)
• ‘I’ ou ‘i’ (Indústrias)
• ‘C’ ou ‘c’ (Comércio )

EXEMPLO:
Bem vindo a calculadora da sua conta de energia:
Digite o tipo de Instalação (R-Residencial, C-Comercial, I-Industrial): R
Digite a quantidade de energia consumida no mês: 1000
Portanto, para o seu caso:
A tarifa por kWh (sem impostos) é de R$ 0.65 reais,
O imposto é de 12%,
e sua conta de energia (com impostos) será de R$ 728 reais.
'''
print('Bem vindo a calculadora da sua conta de energia:')
tipo_de_instalacao = input('Digite o tipo de Instalação (R-Residencial, C-Comercial, I-Industrial):')
qtde_energia_consumida = float(input('Digite a quantidade de energia consumida no mês: '))

def residencial():
    print("Tipo residencial selecionado")
    if qtde_energia_consumida>500:
        preco = 0.65
        imposto = 12
        conta_total = (qtde_energia_consumida * preco) * 1.12
        exibe_resultado(preco,imposto,conta_total)
    else:
        preco = 0.40
        imposto = 10
        conta_total = (qtde_energia_consumida * preco) * 1.10
        exibe_resultado(preco,imposto,conta_total)

def comercial():
    print("Tipo comercial selecionado")
    if qtde_energia_consumida>1000:
        preco = 0.60
        imposto = 16
        conta_total = (qtde_energia_consumida * preco) * 1.16
        exibe_resultado(preco,imposto,conta_total)
    else:
        preco = 0.55
        imposto = 15
        conta_total = (qtde_energia_consumida * preco) * 1.15
        exibe_resultado(preco,imposto,conta_total)

def industrial():
    print("Tipo industrial selecionado")
    if qtde_energia_consumida>5000:
        preco = 0.60
        imposto = 22
        conta_total = (qtde_energia_consumida * preco) * 1.22
        exibe_resultado(preco,imposto,conta_total)
    else:
        preco = 0.55
        imposto = 20
        conta_total = (qtde_energia_consumida * preco) * 1.20
        exibe_resultado(preco,imposto,conta_total)

def default():
    print("valor inválido")
    
def switch(tipo_de_instalacao):
    if tipo_de_instalacao == "R" or tipo_de_instalacao == "r":
        return residencial()
    elif tipo_de_instalacao == "C" or tipo_de_instalacao == "c":
        return comercial()
    elif tipo_de_instalacao == "I" or tipo_de_instalacao == "i":
        return industrial()
    else:
        return default()

def exibe_resultado(preco,imposto,conta_total):
    print('Portanto, para o seu caso:')
    print('A tarifa por kWh (sem impostos) é de R$' + str(preco) + ' reais')
    print('O imposto é de '+ str(imposto) +'%')
    print('e sua conta de energia (com impostos) será de R$' + str(conta_total) + ' reais.')

# Chamando a função switch() para executar a operação apropriada baseada no tipo de instalação
switch(tipo_de_instalacao)
