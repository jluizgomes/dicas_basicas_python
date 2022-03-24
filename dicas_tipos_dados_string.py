# Dicas de Python - Tipos de dados - String

# Variaveis sao espacos de memoria para armazenar dados, podem ser do tipo int, float, string, boolean, list, tuple, dict, etc.
# Podemos criar variaveis com o nome que quisermos
# Ela deve conter apenas letras, numeros e underline
# Não podemos criar variaveis com numeros no inicio
# Não podemos criar variaveis com espaco
# Não podemos criar variaveis com caracteres especiais

# Exemplo de variaveis aceitaveis:
nome = 'Joao'
idade = 20

# Exemplo de variaveis nao aceitaveis:
10nome = 'Joao'
$nome = Joao

# Tipo de dados basicos:
nome = 'Joao' # String
idade = 30 # Int
valor_pi = 3.14 # Float

# Metodos de String:
# Metodos de strings sao funcoes que podem ser aplicadas em strings

# upper() - Converte para maiusculo
nome = 'Joao'
nome.upper()
# Saída: JOAO

# lower() - Converte para minusculo
nome = 'Joao'
nome.lower()
# Saída: joao

# capitalize() - Converte para maiusculo e a primeira letra da string em minusculo
nome = 'joao paulo'
nome.capitalize()
# Saída: Joao Paulo

# title() - Converte para maiusculo e a primeira letra de cada palavra em minusculo
nome = 'joao paulo'
nome.title()
# Saída: Joao Paulo

# strip() - Remove os espaços em branco no inicio e no final da string
nome = ' Joao '
nome.strip()
# Saída: Joao

# lstrip() - Remove os espaços em branco no inicio da string
nome = ' Joao'
nome.lstrip()
# Saída: Joao

# rstrip() - Remove os espaços em branco no final da string
nome = 'Joao '
nome.rstrip()
# Saída: Joao

# replace() - Substitui uma string por outra
nome = 'Meu nome é Joao'
nome.replace('Joao', 'Jorge')
# Saída: Meu nome é Jorge

# split() - Divide uma string em uma lista
nome = 'Meu nome é Jorge'
nome.split()
# Saída: ['Meu', 'nome', 'é', 'Jorge']

# join() - Junta uma lista em uma string
nome = 'Jorge'
sobrenome = 'Gomes'
nome_completo = ' '.join(nome, sobrenome)
# Saída: Jorge Gomes

# count() - Conta quantas vezes uma string aparece em outra
texto = 'Eu gosto de maça, maça é minha fruta favorita'
texto.count('maça')
# Saída: 2