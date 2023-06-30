idade = 15
print(idade > 17)
print(idade < 17)
print(idade >= 17)
print(idade <= 17)
print(idade == 17)
print(idade != 17)

#comparações entre outros tipos
print(True == False)
print('Rafael' == 'rafael')
print('b'>'a')

#operadores booleanos
maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
#você só pode trabalhar se for maior de idade e possuir carteira de trabalho
print(maior_de_idade == True and possui_carteira_de_trabalho == True)
print(maior_de_idade and possui_carteira_de_trabalho)
#Queremos contratar pessoas que ainda não possuem veículo próprio, mas
#já possuam uma carteira de trabalho
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)