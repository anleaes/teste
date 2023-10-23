class Autor:

    def __init__(self, nome, ano_nascimento, email):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        self._email = email
    
    def calcula_idade(self, ano_atual):
        idade = ano_atual - self._ano_nascimento
        return idade
