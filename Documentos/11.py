# Trabalhando com funções

def boas_vindas(nome):
    print(f'Seja bem-vindo, {nome}')
    
boas_vindas('Eduardo')
boas_vindas('Camille')
boas_vindas('Paulo')
boas_vindas('Ruan')

def identidade(nome, idade, cidade):
    print(f'NOME: {nome} \n IDADE: {idade} \n CIDADE: {cidade}')
    
identidade('Eduardo',17,'Angra dos Reis')

def animais(cachorro, gato):
    return f'Meu cachorro chama {cachorro}, e meu gato chama {gato}'

# return retorna um valor para função

print(animais('robson','jonas')+ ', eles são bagunceiros.')