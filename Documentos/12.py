class Aluno:
    def __init__(self, nome, idade, disc):
        self.nome = nome
        self.idade = idade
        self.disciplina = disc
    def estudar(self):
        print(f'{self.nome} está estudando {self.disciplina}')
    def carteirinha(self):
        print(f'NOME: {self.nome} \n IDADE: {self.idade}')
        
eduardo = Aluno('Eduardo', 17, 'Tratamentos Térmicos')

print(eduardo.disciplina)
eduardo.estudar()
eduardo.carteirinha()