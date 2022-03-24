# Dicas de Python - Instruções de Repetição

# Instruções de repetiçoes controlam o fluxo do seu programa com base nas condições que você definir. Isso permite que seu código responda de uma certa maneira, dependendo dessas condições.
# Instruções de repetiçoes são usadas para decidir se uma instrução deve ser executada ou não.
# Instruções de repetiçoes checam se uma condição é verdadeira ou falsa antes de executar o restante do codigo.

# IF
# Se a condição for verdadeira, o bloco de código dentro do if será executado.
idade = 35
if idade >= 18:
    print("Você é maior de idade")
# Saida: Você é maior de idade
    
# IF e ELSE
# Se a condição for verdadeira, o bloco de código dentro do if será executado.
# Se a condição for falsa, o bloco de código dentro do else será executado.
idade = 35
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
# Saida: Você é maior de idade

# IF, ELIF e ELSE
# Se a condição for verdadeira, o bloco de código dentro do if será executado.
# Se a condição for falsa, o bloco de código dentro do elif será executado.
# Se a condição de if e elif forem falsas, o bloco de código dentro do else será executado.
idade = 35
if idade >= 18:
    print("Você é maior de idade")
elif idade >= 16:
    print("Você é adolescente")
else:
    print("Você é menor de idade")
    
# Saida: Você é maior de idade

# WHILE 
# O while é uma instrução de repetição que executa um bloco de código enquanto uma condição for verdadeira.
num = 0
while num < 10:
    print(num)
    num += 1
# Saida: 0 1 2 3 4 5 6 7 8 9

# BREAK
# O break é uma instrução que interrompe a execução de um loop.
while True:
    nome = input("Qual o seu nome? ")
    if nome == 'sair':
        break
    print(f"Olá, {nome}!")
# Saida: Qual o seu nome? João

# FOR
# O for é uma instrução de repetição que executa um bloco de código para cada item de uma coleção.
vogais = ['a', 'e', 'i', 'o', 'u']
for vogal in vogais:
    print(vogal)
# Saida: a e i o u

num = []
for i in range(10):
    num.append(i)
print(num)
# Saida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]