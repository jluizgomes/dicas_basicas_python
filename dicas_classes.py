# Dicas de Python - Classes

# Classes são como se fosse uma função, mas com mais recursos, como atributos e métodos.
# Classes são definidas com a palavra-chave class e seus atributos e métodos são definidos dentro da classe.
# Podemos criar classes que herdam atributos e metodos de outras classes.

# Exemplo de classe
class Aluno(): # Classe Aluno
    def __init__(self, nome, matricula, nome_materia):
        # __init__ é o método construtor, que é executado quando a classe é instanciada, e recebe dois parametros, nome e matricula.
        # self é o objeto que está sendo instanciado, é um parametro obrigatório, e não pode ser omitido.
        # nome e matricula são os parametros que estão sendo passados para o método construtor.
        
        self.nome = nome
        self.matricula = matricula
        self.nome_materia = nome_materia

        # Após criar a classe, podemos adicionar atributos e métodos a ela.
        
        def materia(self):
            nome_materia = self.nome_materia
            print(f'O aluno {self.nome} está cursando a matéria {nome_materia}')
            
aluno = Aluno('João', '12345', 'Programação')
aluno.materia()
# Saida: O aluno João está cursando a matéria Programação

# Herança
# Podemos criar classes que herdam atributos e métodos de outras classes.
class Escola():
    def __init__(self, nome_escola, nome_materia):
        self.nome_escola = nome_escola
        self.nome_materia = nome_materia
    
    def materia(self):
        nome_materia = self.nome_materia
        
class Aluno(Escola):
    materia = Escola.materia('Programação')
    print(f'Aluno está cursando {materia}')

aluno = Aluno('João', '12345', 'Programação')
aluno.materia()
# Saida: Aluno está cursando Programação