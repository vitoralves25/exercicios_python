lanches = ('Hamburguer', 'Suco', 'Pizza', 'Refrigerante')
cont = 0

#for lanche in range(len(lanches)):
    #if lanche % 2 == 0:
    #    print(f'\n{lanches[lanche]:<30}', end='')
    #elif lanche % 1 == 0:
        #print(f'{lanches[lanche]:>30}', end='')
#for carro in range(len(carros)):
    #print(f'Eu vou comprar esse carro: {carros[carro]}: {carro}')


for lanche in range(len(lanches)):
    print(f'Eu quero o {lanche} lanche')


for pos, lanche in enumerate(lanches):
    print(f'Meu lanche está na posição {pos} que é o {lanche}')

#for pos, carro in enumerate(carros):
    #print(f'Quero o carro {carro} da ordem [{pos}]')

# Pra usar pra saber uma posição, eu preciso usar dessa forma acima

print(sorted(lanches))