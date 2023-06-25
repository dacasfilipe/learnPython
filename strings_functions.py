nome_curso = ' Python '
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.find('Py'))
print(nome_curso.replace('Python', 'Linguagem'))
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))
 
teclado = 'Teclado'
print(teclado[2])
teclado.index('l') # pega o índice 3
#usar um indice para acessar a letra c 
teclado.index(-1) # pega o índice -1

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonathan,rafael,carol,camila'
#solução
palavras1 = frase1.split()
palavras2 = frase2.split(',')

print(','.join(palavras1))
print(' & '.join(palavras2))
