# DICAS DE PYTHON - PRINT()

# O print é uma função reservada do Python, isso quer dizer que você não pode atribuir o nome de uma variável como print.
# O print é uma função que imprime na tela o que você quiser.
# O print pode receber vários parâmetros, separados por vírgula.
# O print sempre termina com uma quebra de linha.
# O print pode ser utilizado como uma função, ou como uma expressão.
# Um uso muito comum da função print() é para debugar ou depurar seu código.
# A saida do print é sempre no console ou terminal que você está executando o programa.
# Para quebrar uma linha dentro do print, você deve utilizar o caractere \ (barra invertida).
# Exemplos do uso do print:

# Exemplo 1
print()
# Saida: imprime uma quebra de linha

# Exemplo 2
print('Hello world')
# Saida: imprime Hello world

# Exemplo 3
frutas = ['banana', 'laranja', 'manga']
print(frutas)
# Saida: ['banana', 'laranja', 'manga']

# Formas de concatenar e/ou formatar strings com print:
dia = 24
mes = 'Março'
ano = 2022
dia_semana = 'Quinta' 

# Exemplo 1 - Usando (,) virgula para concatenar strings
print('Hoje é', dia_semana, ' ', str(dia), ' de ', mes, ' de ', str(ano))

# Exemplo 2 - Usando (+) mais para concatenar strings
print('Hoje é dia ' + str(dia) + ' de ' + mes + ' de ' + str(ano) + ' e é dia ' + dia_semana)

# Exemplo 3 - Usando f-strings para concatenar/formatar strings
print(f'Hoje é dia {dia} de {mes} de {ano} e é dia {dia_semana}')

# Exemplo 4 - Usando % (C-style) para concatenar/formatar strings

# Use %s para strings, %d para inteiros, %f para float, %.2f para float com 2 casas decimais

#importando a biblioteca math para usar o math.pi
import math 

nome = 'Jorge'
idade = 35
print('Meu nome é %s, eu tenho %d anos' %(nome, idade))
# Saida: Meu nome é Jorge, eu tenho 35 anos

pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
print('O Valor do pi é %f, Encurtado pi é %0.2f' %(math.pi, math.pi))
# Saida: O Valor do pi é 3.141592653589793, Encurtado pi é 3.14

# Exemplo 5 - Usando format() para concatenar/formatar strings
nome = 'Jorge'
idade = 35
ano_nasc = 1986
print("Meu nome é {}, eu tenho {} anos e nasci no ano de {}".format(nome, idade, ano_nasc))
# Saida: Meu nome é Jorge, eu tenho 35 anos e nasci no ano de 1986