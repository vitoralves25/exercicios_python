lista = [[], []]
for c in range(1,8):
    numeros = int(input(f'Digite o {c}o valor: '))

    if numeros not in lista:
        if numeros % 2 == 0:
            lista[0].append(numeros)
        else:
            lista[1].append(numeros)

lista[0].sort()
lista[1].sort()

print(f'Valores pares: {lista[0]}')
print(f'Valores Impares: {lista[1]}')
