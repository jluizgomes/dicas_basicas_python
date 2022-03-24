# Dicas de Python - Dicionários

# Dicionários
# Dicionários são coleções de dados, onde a chave é um identificador único
cores = {
    'verm': 'vermelho',
    'ver': 'verde',
    'az': 'azul',
}

# Podemos acessar os elementos do dicionário como se fosse uma lista
cores = {
    'verm': 'vermelho',
    'ver': 'verde',
    'az': 'azul',
}
cores['az']
# Saida: 'azul'

# Metodos de dicionários

# get() - Retorna o valor de uma chave
cores.get('verm')
# Saida: 'vermelho'

# keys() - Retorna uma lista com as chaves
cores.keys()
# Saida: dict_keys(['verm', 'ver', 'az'])

# values() - Retorna uma lista com os valores
cores.values()
# Saida: dict_values(['vermelho', 'verde', 'azul'])

# items() - Retorna uma lista com os pares chave/valor
cores.items()
# Saida: dict_items([('verm', 'vermelho'), ('ver', 'verde'), ('az', 'azul')])