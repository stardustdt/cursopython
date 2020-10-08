# Pass e Break

def main():
    pass

while True:
    a = int(input('Digite o número: '))
    if a == 20:
        break


# Lidando com erros
try:
    b = int(input('Número: '))
except ValueError:
    print('Coloque somente números!')
    b = int(input('Número: '))
    
print(b)