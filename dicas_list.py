# Dicas de Python - Listas, Tuplas e Dicionários

# Listas
# Listas são coleções mutáveis de dados. Os colchetes indicam uma lista.
lista = [] # Cria uma lista vazia
vogais = ['a', 'e', 'i', 'o', 'u'] # Cria uma lista com vogais

# Acessando elementos de uma lista
# Podemos acessar os elementos de uma lista através do índice. O índice começa em 0.
vogais = ['a', 'e', 'i', 'o', 'u']
vogais = [0]
# Saída: a

# Modificar elementos de uma lista
vogais = ['a', 'e', 'i', 'o', 'u']
vogais[4] = 'y'
# Saída: ['a', 'e', 'i', 'o', 'y']

# Metodos de listas

# append() - Adiciona um elemento no final da lista
frutas = ['Pera', 'Uva']
frutas.append('Maçã')
# Saída: ['Pera', 'Uva', 'Maçã']

# insert() - Adiciona um elemento em uma posição específica da lista
frutas = ['Pera', 'Uva']
frutas.insert(2, 'Maçã')
# Saída: ['Pera', 'Uva', 'Maçã']

# remove() - Remove um elemento da lista
frutas = ['Pera', 'Uva', 'Maçã']
frutas.remove('Maçã')
# Saída: ['Pera', 'Uva']

# pop() - Remove um elemento da lista e retorna o elemento removido
frutas = ['Pera', 'Uva']
frutas.pop()
# Saída: ['Pera']

frutas.pop(0)
# Saída: ['Uva']

# clear() - Remove todos os elementos da lista
frutas = ['Pera', 'Uva']
frutas.clear()
# Saída: []

# sort() - Ordena uma lista
vogais = ['u', 'o', 'i', 'e', 'a']
vogais.sort()
# Saida: ['a', 'e', 'i', 'o', 'u']

# reverse() - Reverte a ordem de uma lista
vogais = ['u', 'o', 'i', 'e', 'a']
vogais.reverse()
# Saida: ['a', 'e', 'i', 'o', 'u']

# range() - Cria uma lista com números inteiros
nums = list(range(10))
# Saida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Passando dois argumentos para o range(20, 30) cria uma lista com números de 20 a 29
nums = list(range(20, 30))
# Saida: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# len() - Retorna o tamanho de uma lista
lista = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
len(lista)
# Saída: 10