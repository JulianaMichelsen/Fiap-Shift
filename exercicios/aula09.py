class Aluni:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self): # Formato que você deseja que o usuário visualize seu objeto
        return f'Nome: {self.nome}'

    def __repr__(self): # Formato que você deseja visualizar o objeto.
        return f'Nome: {self.nome}'
    