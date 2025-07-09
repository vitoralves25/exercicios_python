numeros = []
maior = menor =  0
for cont in range(0,5):
    numeros.append(int(input(f'Digite seu Número na Posição {cont}: ')))

    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]

print(f'Os valores digitados foram {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if maior == v:
        print(f'{i}...', end='')



print(f'\nO menor valor digitado foi {menor} que está nas posições ', end='')
for i, v in enumerate(numeros):
    if menor == v:
        print(f'{i}...', end='')
