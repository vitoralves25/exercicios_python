numeros = []
for cont in range(0,5):
    numeros.append(int(input(f'Digite seu Número na Posição {cont}: ')))

print(f'Os valores digitados foram {numeros}')
print(f'O maior valor digitado foi {max(numeros)} que está na Posição {numeros.index(max(numeros))}')
print(f'O menor valor digitado foi {min(numeros)} que está na Posição {numeros.index(min(numeros))} ')
