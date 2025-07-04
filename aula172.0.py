#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
#print(valores)
#for valor in valores:
    #print(f'{valor}...')

#for pos, valor in enumerate(valores):
    #print(f'A posição do número é {pos} com o valor {valor}')
#print('Cheguei ao final da lista')


valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um Número: ')))

for pos, num in enumerate(valores):
    print(f'\nO número está na posição {pos + 1} e é o {num}')