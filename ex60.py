from math import factorial
resultado = 1
cont = 0
num = int(input('Digite seu número para ser fatorial: '))
resultado = factorial(num)
print('=>' * 20,  f'Fatorial De {num}',  '<=' * 20)
for c in range(num, 0, -1):
    print(f'{num} * {c} * ', end='')
print(f' = {resultado}', end='')