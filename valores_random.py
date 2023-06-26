# valores aleatórios com random
import random
# Gera um valor de 0.0 a 1.0
print(random.random())

# Gera um valor decimal de Valor mínimo a Valor máximo
print(random.uniform(4,10))
#Gera um valor inteiro
print(random.randint(4,10))

#escolher cor aleatória
cores = ['verde','vermelho','azul']
print(random.choices(cores, k=2))

#embaralhar as cartas
cartas_baralho = ['carta1','carta2','carta3','carta4','carta5']
print(random.shuffle(cartas_baralho))
print(cartas_baralho)

#atalhos vscode

