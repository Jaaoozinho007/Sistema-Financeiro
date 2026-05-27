class Pessoa:
    def __init__ (self, nome, senha):
        self.nome = nome
        self.senha = senha
    
    def verificar_senha (self, senha):
        return self.senha == senha
