# Primeiro jeito de se fazer

#cont = 0
#par = 2
from random import randint
#num = int(input('Digite um número: '))
#segundo_num = int(input('Digite um segundo número: '))
#terceiro_num = int(input('Digite um terceiro número: '))
#quarto_num = int(input('Digite o quarto número: '))

#tupla = (num, segundo_num, terceiro_num, quarto_num)
#print(f'Você digitou esses números {tupla}')
#if 9 in tupla:
#    cont += 1
#    print(f'O Número 9 foi exibido {cont} vez/vezes')
#elif 9 not in tupla:
#    print('O número 9 não foi exibido na listagem')
#if 3 in tupla:
#    resultado = tupla.index(3)
#    print(f'O 3 está na posição {resultado}* posição do índice')
#elif 3 not in tupla:
#    print('Não tem nenhum valor 3 na lista')

#print('Foram inseridos os valores pares', end=' ')
#for pos in tupla:
#    if pos % 2 == 0:
#       print(f'{pos}', end=', ')


# Segundo jeito de se fazer


# Para transformar input em uma tupla, basta fazer esse comando abaixo de parênteses antes do int e depois do último parênteses

num = (int(input('Digite seu Número: ')), int(input('Digite seu Número: ')), int(input('Digite seu Número: ')), int(input('Digite seu Número: ')))
print(num)
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3)+1 }* posição')
else:
    print('Número 3 não foi inserido na lista')

print('Temos os valores pares', end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')






