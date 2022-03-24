# Dicas de Python - Funções

# Funções são blocos de código que podem ser executados de várias formas.
# No Python, as funções são definidas com a palavra reservada def.
# Uma função pode receber parâmetros e retornar um valor.
# Uma função pode ou não receber parâmetros e pode ou não retornar um valor.
# O nome da função é o nome da variável que armazena a função.
# Uma função permite que você organize melhor o seu código.
# Atribua a uma variável uma função segue a mesma regra de criação de variáveis, podendo ter underline no inicio ou para separar as palavras.
# Uma forma comum de nomear uma função é usar camelCase.

# Exemplo de nomes de funções
def nome_aluno():
def nomeAluno():
def NomeAluno():

# Exemplo de função sem parâmetros e sem retorno
def seuNome():
    print('Meu nome é Jorge')

# Exemplo de função com parâmetros e retorno
def soma(a, b):
    return a + b
# O nome da função é soma e o valor retornado é o resultado da soma dos dois parâmetros a e b.

# Exemplo de função com parâmetros com valor padrão e retorno
def soma(a, b = 4): # O valor padrão é 4, se o usuário não informar o valor de b, o valor padrao sera 4.
    return a + b
# O nome da função é soma e o valor retornado é o resultado da soma dos dois parâmetros a e b.

# Para executar uma função, você deve chamar o nome da função.
seuNome()

soma(2, 3)

# Escopo global e local

# As variáveis que são definidas dentro de um corpo de função têm um escopo local e aquelas definidas fora têm um escopo global.
# Isso significa que as variáveis locais podem ser acessadas apenas dentro da função em que são declaradas, enquanto as variáveis globais podem ser acessadas em todo o corpo do programa por todas as funções.
# Quando você chama uma função, as variáveis declaradas dentro dela são trazidas para o escopo.