# \n pula para a linha de baixo

#Um jeito

from random import randint
num_aleatorio = tuple(randint(0,10) for c in range(0,5))
print(f'Os números sorteados foram {num_aleatorio}')
maior_numero = max(num_aleatorio)
menor_numero = min(num_aleatorio)




print(f'O maior número sorteado foi {maior_numero}')
print(f'O menor número sorteado foi {menor_numero}')

# Outro Jeito


num_aleatorio = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
# Para exibir os valores em forma organizada é só fazer com for

for num in num_aleatorio:
    print(f'{num} ', end=' ')
print(f'\nO maior valor sorteado foi {max(num_aleatorio)}')
print(f'O menor valor sorteado foi {min(num_aleatorio)}')





