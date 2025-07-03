r1 = str(input('Valor da primeira reta? '))
r2 = str(input('Valor da segunda reta? '))
r3 = str(input('Valor da terceira reta '))
if r1 and r2 == r3:
    print('Triângulo Equilátero')
elif r1 == r2 and r3 != r1 and r2 or r1 == r3 != r2:
    print('Triângulo Isósceles')
elif r1 != r2 and r1 and r2 != r3:
    print('Triângulo Escaleno')